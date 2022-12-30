import logging
import json
import stringcase

logger = logging.getLogger('take_trial_data')

if __name__ == '__main__':
    conf = json.load(open("configuration.json"))
    logger.info("CONFIGURATION FILE:\n")
    logger.info(conf)
    template = open(f"../_templates/manga template manually.md", 'r').read()
    logger.info("TEMPLATE FILE:\n")
    logger.info(template)
    for manga in conf:
        # read info from configuration file
        name = manga
        read_volumes = conf[manga]["read_volumes"]
        to_read_volumes = conf[manga]["unread_volumes"]
        publisher = conf[manga]["publisher"]
        cover = conf[manga]["cover"]
        editor = conf[manga]["editor"]
        total_volumes = read_volumes + to_read_volumes
        author = conf[manga]["author"]
        bought = conf[manga]["bought"]
        other_tags = ', '.join([stringcase.camelcase(tag.lower().replace(" ", "_")) for tag in [author]])
        missing = conf[manga]["missing"]

        for num_volume in range(1, total_volumes + 1):
            new_read_manga_to_clean = template.format(
                title=name,
                volume=num_volume,
                author=author,
                publisher=publisher,
                cover=cover,
                bought=True if num_volume > bought or num_volume not in missing else False,
                status="Read" if num_volume <= read_volumes else "Unread",
                editor=editor,
                other_tags=other_tags
            ).split("\n")

            new_read_manga = [line.strip() + "\n" for line in new_read_manga_to_clean]

            file_name = f'{name}, Vol {num_volume}.md'
            with open(f"../Readings/Manga/{file_name}", 'w') as f:
                f.writelines(new_read_manga)
                logger.info(f'Create file {file_name}!')
