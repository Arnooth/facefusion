from typing import List, Any, Optional
from argparse import ArgumentParser
import platform
import sys


def create_metavar(ranges : List[Any]) -> str:
	return '[' + str(ranges[0]) + '-' + str(ranges[-1]) + ']'


def create_int_range(start : int, end : int, step : int) -> List[int]:
	int_range = []
	current = start

	while current <= end:
		int_range.append(current)
		current += step
	return int_range


def create_float_range(start : float, end : float, step : float) -> List[float]:
	float_range = []
	current = start

	while current <= end:
		float_range.append(round(current, 2))
		current = round(current + step, 2)
	return float_range


def is_linux() -> bool:
	return to_lower_case(platform.system()) == 'linux'


def is_macos() -> bool:
	return to_lower_case(platform.system()) == 'darwin'


def is_windows() -> bool:
	return to_lower_case(platform.system()) == 'windows'


def to_lower_case(__string__ : Any) -> str:
	return str(__string__).lower()


def has_argument(argument : str) -> bool:
	return any(argv == argument for argv in sys.argv)


def get_argument_value(argument : str) -> Optional[str]:
	try:
		index = sys.argv.index(argument) + 1
		return sys.argv[index]
	except (ValueError, IndexError):
		return None


def get_first(__list__ : Any) -> Any:
	return next(iter(__list__), None)
