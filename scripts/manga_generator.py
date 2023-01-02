import logging
import json
import stringcase
import os

logger = logging.getLogger('take_trial_data')

not_admissible_char = [':', '/', '<', '>', '"', '/', '|', "?", "*", '.', ',', ';', '\'', '-', '’']


def to_admissible_resource(resource):
    replace_char = ''.join(x for x in resource if x not in not_admissible_char)
    to_array = list(filter(None, replace_char.split(" ")))
    to_return = " ".join([el.capitalize() for el in to_array])
    return to_return


def to_tag(element: str) -> str:
    return stringcase.camelcase(to_admissible_resource(element).replace(" ", ""))


def create_folder(path):
    # Check if the "newfolder" directory exists
    if not os.path.exists(path):
        # Create the "newfolder" directory
        os.mkdir(path)


if __name__ == '__main__':
    conf = json.load(open("configuration.json", encoding="utf-8"))
    manga_to_generate = conf["manga"]
    logger.info("CONFIGURATION FILE:\n")
    logger.info(manga_to_generate)
    generation_template = open(f"../_templates/manga template manually.md", 'r', encoding="utf-8").read()
    logger.info("TEMPLATE FILE:\n")
    logger.info(generation_template)
    for manga in manga_to_generate:
        # read info from configuration file
        name = manga
        bought = manga_to_generate[manga]["bought"]
        read_volumes = manga_to_generate[manga]["read_volumes"]
        to_read_volumes = bought - read_volumes
        publisher = manga_to_generate[manga]["publisher"]
        cover = manga_to_generate[manga]["cover"]
        editor = manga_to_generate[manga]["editor"]
        total_volumes = read_volumes + to_read_volumes
        authors: list[str] = manga_to_generate[manga]["author"]

        tags = manga_to_generate[manga]["tags"]
        all_tags = tags
        if isinstance(authors, list):
            all_tags.extend(authors)
        generated_tags: list[str] = [to_tag(tag) for tag in all_tags]
        generated_tags.append(to_tag(name))
        other_tags = ', '.join(generated_tags)
        missing = manga_to_generate[manga]["missing"]
        admissible_name = to_admissible_resource(name)

        for num_volume in range(1, total_volumes + 1):
            new_read_manga = generation_template.format(
                title=admissible_name,
                volume=num_volume,
                author=authors,
                publisher=publisher,
                cover=cover,
                bought=False if num_volume > bought or num_volume in missing else True,
                status="Read" if num_volume <= read_volumes else "Unread",
                editor=editor,
                other_tags=other_tags
            )

            file_name = f'{admissible_name}, Vol {num_volume}.md'
            create_folder(f"../Readings/Manga/{admissible_name}/")
            with open(f"../Readings/Manga/{admissible_name}/{file_name}", 'w', encoding="utf-8") as f:
                f.writelines(new_read_manga)
                logger.info(f'Create file {admissible_name}!')
    logger.info("ALL MANGA GENERATED")

    logger.info("START COMPLETE MANGA:")
    completed_template = open(f"../_templates/manga template completed.md", 'r', encoding="utf-8").read()
    logger.info("TEMPLATE FILE:\n")
    logger.info(completed_template)
    for completed in conf["completed"]:
        admissible_name = to_admissible_resource(completed)
        file_name = f'{admissible_name}.md'

        bought = manga_to_generate[completed]["bought"]
        cover = manga_to_generate[completed]["cover"]
        authors: list[str] = manga_to_generate[completed]["author"]

        completed_manga = completed_template.format(
            title=admissible_name,
            author=authors,
            cover=cover,
            total_volume=bought
        )

        create_folder(f"../Readings/Manga/Complete")
        with open(f"../Readings/Manga/Complete/{file_name}", 'w', encoding="utf-8") as f:
            f.writelines(completed_manga)
            logger.info(f'Create file {admissible_name}!')
    logger.info("ALL Completed Manga GENERATED")
