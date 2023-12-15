from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS = 'results'
#(BASE_DIR / RESULTS).mkdir(exist_ok=True)

BOT_NAME = 'pep_parse'


NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE, ]


ROBOTSTXT_OBEY = True


FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
