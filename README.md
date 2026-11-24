# datecalc

Everyday date arithmetic from the command line: days between two dates, adding and subtracting calendar days or business days, and the basic facts about any date. For planners, writers, and anyone counting down to a deadline without opening a calendar app.

## Quickstart

```
python3 datecalc.py --help
python3 datecalc.py info 2026-11-23
```

## Usage

```
usage: datecalc.py [-h] {between,add,sub,info} ...

  between DATE1 DATE2          Absolute number of days between the dates
  add DATE N [--business]      Date N days after DATE (N may be negative)
  sub DATE N [--business]      Date N days before DATE
  info DATE                    Weekday, day of year, ISO week, leap year,
                               days in month

All dates are ISO format YYYY-MM-DD. --business counts only Monday-Friday
days, stepping one calendar day at a time; the starting date is never
counted.
```

## Examples

```
$ python3 datecalc.py between 2026-01-01 2026-12-31
364

$ python3 datecalc.py add 2026-11-23 30
2026-12-23

$ python3 datecalc.py add 2026-11-20 1 --business
2026-11-23

$ python3 datecalc.py info 2026-11-23
Date: 2026-11-23
Weekday: Monday
Day of year: 327
ISO week: 48
Leap year: no
Days in month: 30
```

## Configuration

None — all options are command-line flags.

## Limitations

Dates only — no times, no time zones. Business days mean Monday-Friday; public holidays are not subtracted, because holiday calendars differ by place. ISO format only; other date formats are rejected rather than guessed.

## License

MIT — see `LICENSE`.

By Dr. Brent Allen Jensen, Radical Blueprinting Research.

## Support this work

If this tool saved you time, you can support more open work like it:

- **BTC:** `15McijPo79Zx58NGyEf2PvaPtGqGmpztWn`
- **ETH:** `0x8C25164E9234E6A30b8E44485B79c5cE8419cF2B`

Thank you.
