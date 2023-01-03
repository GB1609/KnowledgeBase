---

database-plugin: basic

---

```yaml:dbfolder
name: Manga Database
description: Database of all manga
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
    width: 786
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
    options:
      - { label: "Naoki Urasawa", backgroundColor: "hsl(82, 95%, 90%)"}
      - { label: "Makoto Shinkai", backgroundColor: "hsl(355, 95%, 90%)"}
      - { label: "Masashi Kishimoto", backgroundColor: "hsl(14, 95%, 90%)"}
      - { label: "Katsuhiro Ōtomo", backgroundColor: "hsl(69, 95%, 90%)"}
      - { label: "Hajime Isayama", backgroundColor: "hsl(349, 95%, 90%)"}
      - { label: "Kentarō Miura, Kōji Mori", backgroundColor: "hsl(131, 95%, 90%)"}
      - { label: "Muneyuki Kaneshiro, Yusuke Nomura", backgroundColor: "hsl(136, 95%, 90%)"}
      - { label: "Takehiko Inoue", backgroundColor: "hsl(240, 95%, 90%)"}
      - { label: "Ken Wakui", backgroundColor: "hsl(161, 95%, 90%)"}
      - { label: "Sui Ishida", backgroundColor: "hsl(130, 95%, 90%)"}
      - { label: "Yōichi Takahashi", backgroundColor: "hsl(182, 95%, 90%)"}
      - { label: "Tatsuki Fujimoto", backgroundColor: "hsl(302, 95%, 90%)"}
      - { label: "Tsugumi Ōba", backgroundColor: "hsl(261, 95%, 90%)"}
      - { label: "Giorgio Battisti, Luca Molinaro", backgroundColor: "hsl(4, 95%, 90%)"}
      - { label: "Gō Nagai", backgroundColor: "hsl(209, 95%, 90%)"}
      - { label: "Akira Toriyama", backgroundColor: "hsl(197, 95%, 90%)"}
      - { label: "Nagabe", backgroundColor: "hsl(11, 95%, 90%)"}
      - { label: "Hiroyuki Takei", backgroundColor: "hsl(262, 95%, 90%)"}
      - { label: "Nakaba Suzuki", backgroundColor: "hsl(229, 95%, 90%)"}
      - { label: "Kaiu Shirai", backgroundColor: "hsl(62, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
  bought:
    input: select
    accessorKey: bought
    key: bought
    id: bought
    label: bought
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
  manga:
    input: text
    accessorKey: manga
    key: manga
    id: manga
    label: manga
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    isSorted: false
    isSortedDesc: false
    width: 420
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
  status:
    input: text
    accessorKey: status
    key: status
    id: status
    label: status
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
  cell_size: "normal"
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
  source_data: "current_folder"
  source_form_result: "root"
  source_destination_path: "/"
  row_templates_folder: "/"
  current_row_template: ""
  pagination_size: 50
  font_size: 10
  enable_js_formulas: false
  formula_folder_path: "/"
  inline_default: false
  inline_new_position: "last_field"
  date_format: "yyyy-MM-dd"
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: true
filters:
  enabled: false
  conditions:
```