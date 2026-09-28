// Run: CHROME_BIN=/path/to/chrome node scripts/tests/orbit-browser.test.cjs URL [SCREENSHOT_DIRECTORY]
// Requires Playwright. Tests the served page, its real controls and rendered equations.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {chromium} = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: true,
        ...(process.env.CHROME_BIN ? {executablePath: process.env.CHROME_BIN} : {})
    });
    try {
        const context = await browser.newContext({viewport: {width: 1440, height: 1000}});
        const page = await context.newPage();
        const errors = [];
        page.on('pageerror', error => errors.push(error.message));
        page.on('requestfailed', request => console.error('Request failed:', request.url(), request.failure()?.errorText));
        await page.goto(process.argv[2], {waitUntil: 'networkidle'});
        console.log('Page loaded; checking equation rendering.');
        try {
            await page.waitForFunction(() => document.querySelectorAll('mjx-container').length > 100);
        } catch (error) {
            console.error(await page.evaluate(() => ({
                mathNodes: document.querySelectorAll('mjx-container').length,
                mathStartup: Boolean(window.MathJax?.startup),
                pageTitle: document.title
            })));
            throw error;
        }
        await page.evaluate(() => MathJax.startup.promise);
        assert.equal(await page.locator('mjx-merror, [data-mjx-error]').count(), 0, 'All TeX must render');
        assert.equal(await page.locator('#depth').inputValue(), '0.64');
        await page.getByRole('button', {name: 'L = 2, four lobes', exact: true}).click();
        await page.getByRole('combobox', {name: 'Position response', exact: true}).selectOption('1');
        assert.match(await page.locator('#responseNote').innerText(), /Smooth/);
        await page.getByRole('button', {name: 'Align one extra radial maximum', exact: true}).click();
        await page.getByText('State & orbit details', {exact: true}).click();
        assert.match(await page.locator('#stateReturn').innerText(), /7.84%/);
        assert.match(await page.locator('#orbitCondition').innerText(), /0.360 R/);
        await page.getByRole('combobox', {name: 'Relative phase offset', exact: true}).selectOption('0.5');
        assert.match(await page.locator('#stateReturn').innerText(), /100.00%/);
        await page.getByRole('combobox', {name: 'Relative phase offset', exact: true}).selectOption('sqrt2');
        assert.match(await page.locator('#stateReturn').innerText(), /prevents exact state recurrence/);
        await page.getByRole('button', {name: 'Restore ideal orbit', exact: true}).click();
        await page.getByText('State & orbit details', {exact: true}).click();
        await page.getByRole('button', {name: 'L = 3, six lobes', exact: true}).click();
        const canvas = await page.locator('#orbitCanvas').boundingBox();
        await page.mouse.move(canvas.x+canvas.width/2, canvas.y+canvas.height/2);
        await page.mouse.down();
        await page.mouse.move(canvas.x+canvas.width/2+85, canvas.y+canvas.height/2+45);
        await page.mouse.up();
        const screenshots = process.argv[3];
        if (screenshots) {
            fs.mkdirSync(screenshots, {recursive: true});
            await page.screenshot({path: path.join(screenshots, 'desktop.png')});
        }
        for (const size of [{width: 390,height: 844}, {width: 768,height: 1024}, {width: 1440,height: 1000}]) {
            await page.setViewportSize(size);
            await page.evaluate(() => window.scrollTo(0,0));
            const geometry = await page.evaluate(() => {
                const canvas = document.getElementById('orbitCanvas').getBoundingClientRect();
                return {
                    width: document.documentElement.scrollWidth,
                    viewport: window.innerWidth,
                    canvas: {width:canvas.width,height:canvas.height},
                    mathErrors: document.querySelectorAll('mjx-merror, [data-mjx-error]').length
                };
            });
            if (geometry.width > geometry.viewport+1) {
                console.error('Overflow:', size, geometry, await page.evaluate(() =>
                    [...document.querySelectorAll('body *')].filter(e => {
                        const r = e.getBoundingClientRect();
                        return r.width && !e.closest('mjx-container') && !e.closest('.nav-links') && (r.right > innerWidth+1 || r.left < -1);
                    }).slice(0,20).map(e => ({tag:e.tagName,className:e.className,text:e.textContent.slice(0,90),right:e.getBoundingClientRect().right,width:e.getBoundingClientRect().width}))
                ));
                if (screenshots) await page.screenshot({path:path.join(screenshots,'overflow.png')});
            }
            assert.ok(geometry.width <= geometry.viewport+1, 'Page must not overflow horizontally');
            assert.ok(geometry.canvas.width > 200 && geometry.canvas.height > 150, 'Controls must leave room for the orbit');
            assert.equal(geometry.mathErrors, 0);
            await page.getByRole('combobox', {name: 'Position response', exact: true}).selectOption('0.5');
            await page.getByRole('combobox', {name: 'Position response', exact: true}).selectOption('1');
            if (screenshots && size.width === 390) await page.screenshot({path: path.join(screenshots,'mobile.png')});
        }
        // Inspect new formulas below the fold as rendered, including the bridge and response.
        await page.getByRole('heading', {name: 'From a spatial trajectory to the picture', exact: true}).scrollIntoViewIfNeeded();
        if (screenshots) await page.screenshot({path: path.join(screenshots,'spatial-bridge.png')});
        assert.deepEqual(errors, [], 'No page JavaScript exceptions');
        console.log('PASS: browser controls, smooth radius, phase recurrence, doubled depth, all TeX, and three responsive viewport sizes.');
    } finally {
        await browser.close();
    }
})().catch(error => {console.error(error); process.exitCode = 1;});
