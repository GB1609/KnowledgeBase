---
banner: "![[book_banner.jpg]]"
banner_y: 0.78
banner_lock: true
---

## All Books
---
Displays all books from the Books folder.

```dataview
table author, ("![coverimg|95](" + cover +")") as cover
from #book and -"Assets/Templates"
sort file.name asc
```
--- 
## Book Tracker
---
Displays and groups all books based on their Status.
```dataview
table rows.file.link as book
from "Readings/Books" and -"Readings/Books/Review" and #book 
group by status
sort status
```
--- 
## List of Read Books
---
Displays all books with the "Read" status.

```dataview
table author, ("![coverimg|95](" + cover +")") as cover
from #book 
where status="Read"
sort file.name asc
```
