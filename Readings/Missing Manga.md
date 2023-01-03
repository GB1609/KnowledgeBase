---
banner: "![[manga_banner.jpg]]"
banner_y: 0.35778
banner_lock: true
---

# Missing Manga

```dataviewjs
dv.table(["Manga", "Title", "Volume"],
    dv.pages("#manga")
        .where(b => b.bought == false)
        .sort(m => m.manga)
        .map(m => [m.manga, m.title, m.vol]))
```

# Last Bought Volume For Manga

```dataviewjs
let all_manga = dv.pages("#manga")
    .where(b => b.bought == true)
    .groupBy(m => m.manga);
let completed = dv.pages("#completeManga").map(c => c.title.toLowerCase());
let manga = all_manga.filter(x => !completed.includes(x.key.toLowerCase()));
dv.table(["Manga", "Volume"], manga.map(m => {
    let vols = m.rows.vol;
    let max = Math.max(...vols);
    return [m.key, max]
}))
```

