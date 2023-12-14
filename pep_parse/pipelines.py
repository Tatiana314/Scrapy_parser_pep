import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1] / 'results'
FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:
    def open_spider(self, spider):
        BASE_DIR.mkdir(parents=True, exist_ok=True)
        self.quantity_peps = defaultdict(int)
        self.file_path = BASE_DIR / FILE_NAME.format(
            datetime.now().strftime("%y-%m-%d_%H-%M-%S")
        )

    def process_item(self, item, spider):
        self.quantity_peps[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.file_path, mode='w', encoding='utf-8') as f:
            csv.writer(f, csv.unix_dialect).writerows(
                (('Статус', 'Количество'),
                 *self.quantity_peps.items(),
                 ('Total', sum(self.quantity_peps.values())))
            )
