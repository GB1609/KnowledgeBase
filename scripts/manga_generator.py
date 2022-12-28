import logging
import json
import stringcase

logger = logging.getLogger('take_trial_data')

template = """
    ---
    tag: [📚Manga, {other_tags}]
    title: "{title}, Vol {volume}"
    vol: {volume}
    author: [{author}]
    publisher: {publisher}
    cover: {cover}
    status: {status}
    editor: {editor}
    ---


    - Metadata:
        - **Author:** `= this.author`
        - **Status:** `= this.status`
        - **Vol:** `= this.vol`
    
    This is the book note. Switch to Edit mode (Ctrl+E or Command+E on the Mac) to see the book note's YAML frontmatter.
    """

if __name__ == '__main__':
    manga_infos = json.load(open("configuration.json"))
    for manga in manga_infos:
        # read info from configuration file
        name = manga
        read_volumes = manga_infos[manga]["read_volumes"]
        to_read_volumes = manga_infos[manga]["unread_volumes"]
        publisher = manga_infos[manga]["publisher"]
        cover = manga_infos[manga]["cover"]
        editor = manga_infos[manga]["editor"]
        total_volumes = read_volumes + to_read_volumes
        author = manga_infos[manga]["author"]
        other_tags = ', '.join([stringcase.camelcase(tag.lower().replace(" ", "_")) for tag in [author]])

        for num_volume in range(1, total_volumes + 1):
            new_read_manga_to_clean = template.format(
                title=name,
                volume=num_volume,
                author=author,
                publisher=publisher,
                cover=cover,
                status="Read" if num_volume <= read_volumes else "Unread",
                editor=editor,
                other_tags=other_tags
            ).split("\n")

            new_read_manga = [line.strip() + "\n" for line in new_read_manga_to_clean]

            file_name = f'{name}, Vol {num_volume}.md'
            with open(f"../Readings/Manga/{file_name}", 'w') as f:
                f.writelines(new_read_manga)
                logger.info(f'Create file {file_name}!')
