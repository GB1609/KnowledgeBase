---
banner: "![[banner.jpg]]"
banner_y: 0.752
banner_lock: true
---

## All Books
---
Displays all books from the Books folder.

```dataview
table author, ("![coverimg|95](" + cover +")") as cover
from "Readings/Books"
sort file.name asc
```
--- 
## Book Tracker
---
Displays and groups all books based on their Status.
```dataview
table rows.file.link as book
from "Readings/Books"
group by status
sort status
```
--- 
## List of Read Books
---
Displays all books with the "Read" status.

```dataview
table rows.file.link as book
from "Readings/Books"
where status = "Read"
```
