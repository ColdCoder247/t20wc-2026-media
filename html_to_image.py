
import asyncio
from playwright.async_api import async_playwright
import os

async def convert_html_to_png(html_path, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1200, "height": 1600})
        await page.goto(f"file://{os.path.abspath(html_path)}")
        await page.wait_for_timeout(1000)
        await page.screenshot(path=output_path, full_page=True)
        await browser.close()

def convert(html_file, png_file):
    asyncio.run(convert_html_to_png(html_file, png_file))
