from collections import defaultdict
from datetime import datetime
from pathlib import Path


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        feeds = spider.settings.get('FEEDS')
        feed_path = list(feeds.keys())[0]
        results_dir = Path(feed_path).parent
        results_dir.mkdir(exist_ok=True)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = results_dir / f'status_summary_{now}.csv'
        total = sum(self.statuses.values())

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('Статус,Количество\n')
            for status, count in self.statuses.items():
                file.write(f'{status},{count}\n')
            file.write(f'Total,{total}\n')
