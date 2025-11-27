from playwright.sync_api import Page

def test_responsive_layout(page: Page, assert_snapshot):
    page.goto("file:///app/index.html")

    # Mobile
    page.set_viewport_size({"width": 375, "height": 812})
    assert_snapshot(page)

    # Tablet
    page.set_viewport_size({"width": 768, "height": 1024})
    assert_snapshot(page)

    # Small Laptop
    page.set_viewport_size({"width": 1024, "height": 768})
    assert_snapshot(page)
