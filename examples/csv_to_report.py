import csv
from pathlib import Path


def csv_to_report(input_file: str, output_file: str) -> dict:
    """
    Reads a CSV file, performs basic aggregation,
    and writes a processed report.
    """

    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError("Input CSV file not found")

    total_rows = 0

    with input_path.open(mode="r", newline="") as infile:
        reader = csv.reader(infile)
        header = next(reader, None)

        for _ in reader:
            total_rows += 1

    with output_path.open(mode="w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["metric", "value"])
        writer.writerow(["total_rows", total_rows])

    return {
        "input_file": str(input_path),
        "output_file": str(output_path),
        "rows_processed": total_rows,
        "status": "report_generated"
    }
