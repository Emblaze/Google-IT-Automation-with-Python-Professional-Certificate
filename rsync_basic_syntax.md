# rsync cheat-sheet

## rsync basic syntax

```bash
$ rsync [Options] [Source-Files-Dir] [Destination]
[...]
```

| Options | Uses                                            |
|---------|-------------------------------------------------|
| -v      | Verbose output                                  |
| -q      | Suppress message output                         |
| -a      | Archive files and directory while synchronizing |
| -r      | Sync files and directories recursively          |
| -b      | Take the backup during synchronization          |
| -z      | Take the backup during synchronization          |

## Examples

Example:

1. Copy or sync files locally:

```bash
$ rsync -zvh [Source-Files-Dir] [Destination]
[...]
```

2. Copy or sync directory locally:

```bash
$ rsync -zavh [Source-Files-Dir] [Destination]
[...]
```

3. Copy files and directories recursively locally:

```bash
$ rsync -zrvh [Source-Files-Dir] [Destination]
[...]
```

To learn more about rsync basic command, check out [this link](https://www.linuxtechi.com/rsync-command-examples-linux/).
