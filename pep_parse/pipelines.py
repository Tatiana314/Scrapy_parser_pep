import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, RESULTS

FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:
    def create_results_folder(self):
        if not (BASE_DIR / RESULTS).exists():
            (BASE_DIR / RESULTS).mkdir()

    def open_spider(self, spider):
        self.quantity_peps = defaultdict(int)

    def process_item(self, item, spider):
        self.quantity_peps[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.create_results_folder()
        with open(BASE_DIR / RESULTS / FILE_NAME.format(
            datetime.now().strftime("%y-%m-%d_%H-%M-%S")
        ), mode='w', encoding='utf-8') as f:
            csv.writer(f, csv.unix_dialect, quoting=csv.QUOTE_NONE).writerows((
                ('Статус', 'Количество'),
                *self.quantity_peps.items(),
                ('Total', sum(self.quantity_peps.values()))
            ))
