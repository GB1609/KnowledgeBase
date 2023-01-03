---
banner: "![[book_banner.jpg]]"
banner_y: 0.752
banner_lock: true
---

## All Manga
---
Displays all manga from the Manga folder.

```dataview
table author, ("![coverimg|95](" + cover +")") as cover
from "Readings/Manga"
where bought=True
sort volume asc
```

