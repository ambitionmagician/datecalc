#!/usr/bin/env python3
"""
Date calculation tool for everyday date arithmetic.

Examples:
    $ python datecalc.py between 2026-01-01 2026-12-31
    364

    $ python datecalc.py add 2026-11-23 30
    2026-12-23
"""

import argparse
import calendar
import sys
from datetime import datetime, timedelta


def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def cmd_between(args):
    d1 = parse_date(args.date1)
    d2 = parse_date(args.date2)
    if d1 is None or d2 is None:
        print("Invalid date", file=sys.stderr)
        sys.exit(2)
    print(abs((d2 - d1).days))


def count_business_days(start_date, n):
    if n == 0:
        return start_date
    direction = 1 if n > 0 else -1
    current = start_date
    counted = 0
    while counted < abs(n):
        current += timedelta(days=direction)
        if current.weekday() < 5:
            counted += 1
    return current


def cmd_add(args):
    d = parse_date(args.date)
    if d is None:
        print("Invalid date", file=sys.stderr)
        sys.exit(2)
    try:
        n = int(args.n)
    except ValueError:
        print("Invalid N", file=sys.stderr)
        sys.exit(2)
    if args.business:
        result = count_business_days(d, n)
    else:
        result = d + timedelta(days=n)
    print(result.isoformat())


def cmd_sub(args):
    d = parse_date(args.date)
    if d is None:
        print("Invalid date", file=sys.stderr)
        sys.exit(2)
    try:
        n = int(args.n)
    except ValueError:
        print("Invalid N", file=sys.stderr)
        sys.exit(2)
    if args.business:
        result = count_business_days(d, -n)
    else:
        result = d - timedelta(days=n)
    print(result.isoformat())


def cmd_info(args):
    d = parse_date(args.date)
    if d is None:
        print("Invalid date", file=sys.stderr)
        sys.exit(2)
    year = d.year
    print(f"Date: {d.isoformat()}")
    print(f"Weekday: {d.strftime('%A')}")
    print(f"Day of year: {d.timetuple().tm_yday}")
    print(f"ISO week: {d.isocalendar()[1]}")
    print(f"Leap year: {'yes' if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 'no'}")
    print(f"Days in month: {calendar.monthrange(year, d.month)[1]}")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    p_between = subparsers.add_parser("between")
    p_between.add_argument("date1")
    p_between.add_argument("date2")
    p_between.set_defaults(func=cmd_between)

    p_add = subparsers.add_parser("add")
    p_add.add_argument("date")
    p_add.add_argument("n")
    p_add.add_argument("--business", action="store_true")
    p_add.set_defaults(func=cmd_add)

    p_sub = subparsers.add_parser("sub")
    p_sub.add_argument("date")
    p_sub.add_argument("n")
    p_sub.add_argument("--business", action="store_true")
    p_sub.set_defaults(func=cmd_sub)

    p_info = subparsers.add_parser("info")
    p_info.add_argument("date")
    p_info.set_defaults(func=cmd_info)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
