---

database-plugin: basic

---

```yaml:dbfolder
name: Book Database
description: Info about all books
columns:
  __file__:
    key: __file__
    id: __file__
    input: markdown
    label: File
    accessorKey: __file__
    isMetadata: true
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 0
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
  author:
    input: tags
    accessorKey: author
    key: author
    id: author
    label: author
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 378
    options:
      - { label: "Dan Brown", backgroundColor: "hsl(178, 95%, 90%)"}
      - { label: "Maurice Leblanc", backgroundColor: "hsl(287, 95%, 90%)"}
      - { label: "Erich Gamma", backgroundColor: "hsl(28, 95%, 90%)"}
      - { label: "Richard Helm", backgroundColor: "hsl(247, 95%, 90%)"}
      - { label: "Craig Larman", backgroundColor: "hsl(132, 95%, 90%)"}
      - { label: "Ralph Johnson", backgroundColor: "hsl(59, 95%, 90%)"}
      - { label: "John M. Vlissides", backgroundColor: "hsl(6, 95%, 90%)"}
      - { label: "Stephen King", backgroundColor: "hsl(352, 95%, 90%)"}
      - { label: "Vlad Khononov", backgroundColor: "hsl(222, 95%, 90%)"}
    config:
      enable_media_view: false
      link_alias_enabled: false
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      wrap_content: false
  status:
    input: select
    accessorKey: status
    key: status
    id: status
    label: status
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "Read", backgroundColor: "hsl(0, 95%, 90%)"}
      - { label: "Unread", backgroundColor: "hsl(0, 95%, 90%)"}
      - { label: "Read In Progress", backgroundColor: "hsl(0, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
  ratings:
    input: select
    accessorKey: ratings
    key: ratings
    id: ratings
    label: ratings
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 256
    options:
      - { label: "⭐⭐⭐⭐⭐", backgroundColor: "hsl(0,0%,0%)"}
      - { label: "⭐⭐⭐⭐", backgroundColor: "hsl(0,0%,0%)"}
      - { label: "⭐⭐⭐", backgroundColor: "hsl(0,0%,0%)"}
      - { label: "⭐⭐", backgroundColor: "hsl(0,0%,0%)"}
      - { label: "⭐", backgroundColor: "hsl(0,0%,0%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      wrap_content: false
  start_read:
    input: text
    accessorKey: start_read
    key: start_read
    id: start_read
    label: start_read
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
  end_read:
    input: text
    accessorKey: end_read
    key: end_read
    id: end_read
    label: end_read
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 288
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
  cover:
    input: text
    accessorKey: cover
    key: cover
    id: cover
    label: cover
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
  title:
    input: text
    accessorKey: title
    key: title
    id: title
    label: title
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
config:
  remove_field_when_delete_column: false
  cell_size: "compact"
  sticky_first_column: true
  group_folder_column: ""
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  source_data: "current_folder_without_subfolders"
  source_form_result: ""
  source_destination_path: "/"
  row_templates_folder: ""
  current_row_template: ""
  pagination_size: 10
  font_size: 16
  enable_js_formulas: false
  formula_folder_path: "/"
  inline_default: false
  inline_new_position: "last_field"
  date_format: "yyyy-MM-dd"
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: false
filters:
  enabled: false
  conditions:
```