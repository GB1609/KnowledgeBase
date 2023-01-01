import logging
import json
import stringcase

logger = logging.getLogger('take_trial_data')


def to_tag(element: str) -> str:
    return stringcase.camelcase(str.lower(element).replace(" ", "_"))


if __name__ == '__main__':
    conf = json.load(open("configuration.json", encoding="utf-8"))
    logger.info("CONFIGURATION FILE:\n")
    logger.info(conf)
    template = open(f"../_templates/manga template manually.md", 'r', encoding="utf-8").read()
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
        authors: list[str] = conf[manga]["author"]
        bought = conf[manga]["bought"]
        tags = conf[manga]["tags"]
        all_tags = tags
        if isinstance(authors, list):
            all_tags.extend(authors)
        generated_tags: list[str] = [to_tag(tag) for tag in all_tags]
        other_tags = ', '.join(generated_tags)
        missing = conf[manga]["missing"]

        for num_volume in range(1, total_volumes + 1):
            new_read_manga = template.format(
                title=name,
                volume=num_volume,
                author=authors,
                publisher=publisher,
                cover=cover,
                bought=False if num_volume > bought or num_volume in missing else True,
                status="Read" if num_volume <= read_volumes else "Unread",
                editor=editor,
                other_tags=other_tags
            )

            file_name = f'{name}, Vol {num_volume}.md'
            with open(f"../Readings/Manga/{file_name}", 'w', encoding="utf-8") as f:
                f.writelines(new_read_manga)
                logger.info(f'Create file {file_name}!')
