import scrapy


class SteamspiderSpider(scrapy.Spider):
    name = "steamspider"
    allowed_domains = ["store.steampowered.com"]
    base_url = "https://store.steampowered.com/search/?ignore_preferences=1&sort_by=&sort_order=0&category1=998&filter=topsellers&ndl=1&page=%s"
    page = 1
    start_urls = [base_url % page]

    def parse(self, response):
        games = response.css("a.search_result_row.ds_collapse_flag")

        for game in games:
            url = game.css("a").attrib["href"]
            sep = "/?"
            url_clean = url.split(sep, 1)[0]
            yield response.follow(url_clean, cookies={"birthtime": 880909201,
                                                      "wants_mature_content": 1},
                                            callback=self.get_tags)

        # Parse only first 40 pages.
        # Each page contains 25 games, so the total number is 40*25 = 1000 games
        if self.page < 40:
            self.page += 1
            next_page = self.base_url % self.page
            yield response.follow(next_page, callback=self.parse)

    def get_tags(self, response):
        tags = response.css("a.app_tag")
        name = response.css("div.apphub_AppName::text").get()
        if name is None:
            name = response.css("h2.pageheader::text").get()
        yield {
            "name": name,
            "url": response.url,
            "tags": [tag.css("a::text").get().strip() for tag in tags]
        }
