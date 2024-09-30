# Profit and Loss (PnL) Calculator

The goal of this problem is to build a tool to read some stock market trading reports that are in the form of a PDF file, convert them into structured CSV data and then calculate the net profit or loss for the total investments made for all stocks that were sold. (The method to do the same will be explained in [Step 1](#step-1-read-and-clean-easy-pdf).)

You will need to build a CLI (Command Line Interface) tool to solve this problem. The CLI will take in a subcommand and each subcommand will have an input file path (`--input`) and an output file path (`--output`) as an argument.

Set up the project in the language of your choice. Define the basic structure of the program, and get a working implementation that takes in an input file and writes a file at the provided output file path after processing it in the way specified in the respective Step.

Please include documentation (in a file called `SETUP.md`) on any prerequisites we would need to have installed to run your program, including the language that we'll need to have set up.

For each CSV file that you generate, you need to run the `diff` command (for Linux and macOS, `FC` for Windows) to ensure that the CSV produced by your tool is the same as the expected output.

## Input

You are provided with sample PDF files for basic stock market reports. Each Step utilizes a different PDF file and expects you to write the output to a specifically named CSV/XLSX file.

1. [Investments-1.pdf](./input/Investments-1.pdf)
2. [Investments-2.pdf](./input/Investments-2.pdf)
3. [Investments-3.pdf](./input/Investments-3.pdf)

## Output

You are required to write the output CSV file to the `output/` folder as specified in the respective Step.

For the submission to be accepted you will need to commit and push the output folder with the processed CSV/XLSX files along with the code of the tool to the main branch of the repository.

## Step 1: Read and Clean Easy PDF

You need to write a tool that reads `input/Investments-1.pdf` and writes the CSV conversion of the PDF to `output/Investments-1.csv`.

The command to run the tool should look like this:

```bash
<program> convert_basic --input input/Investments-1.pdf --output output/Investments-1.csv
```

The header of the CSV should not be hard coded in the tool but it should be extracted from the PDF file.

### Test Code 1

On Linux and macOS:

```bash
diff output/Investments-1.csv reference/Investments-1.csv
```

or for Windows:

```bash
FC output/Investments-1.csv reference/Investments-1.csv
```

The output of the above command should be empty for your solution to pass.

## Step 2: Calculate Profit and Loss (PnL)

You need to now modify the tool to take in an additional parameter `--pnl-output` which takes in the path to the CSV output file where we need to write the calculated profit or loss of each stock sold.

You only need to calculate the profit or loss of the stocks that were sold, i.e., the rows that have a `Date Sold` value.

To calculate the profit or loss, you need to subtract the sale price from the purchase price and multiply the difference by the number of shares purchased.

$$
Profit = (Sale\ Price - Purchase\ Price) * Shares\ Purchased
$$

You need to report the total profit or loss as an aggregate for all the stocks sold.

The command to run the tool should look like this:

```bash
<program> convert_basic --input input/Investments-1.pdf --output output/Investments-1.csv --pnl-output output/Investments-1-PnL.csv
```

The output file should have the following content:

| Stock Symbol | Net Profit/Loss (PnL) |
| ------------ | --------------------- |
| AAPL         | `AAPL PnL`            |
| MSFT         | `MSFT PnL`            |
| TSLA         | `TSLA PnL`            |
| AMZN         | `AMZN PnL`            |
| GOOG         | `GOOG PnL`            |
| NFLX         | `NFLX PnL`            |

Where `AAPL PnL` is the profit or loss of AAPL as calculated from `Investments-1.pdf` file.

### Test Code 2

On Linux and macOS:

```bash
diff output/Investments-1-PnL.csv reference/Investments-1-PnL.csv
```

or for Windows:

```bash
FC output/Investments-1-PnL.csv reference/Investments-1-PnL.csv
```

The output of the above command should be empty for your solution to pass.

## Step 3: Read and Clean the Misaligned Header PDF

You need to write a tool that reads `input/Investments-2.pdf` and writes the CSV conversion of the PDF to `output/Investments-2.csv`.
In this PDF file, the header is not aligned.

The command to run the tool should look like this:

```bash
<program> convert_misaligned_headers --input input/Investments-2.pdf --output output/Investments-2.csv
```

The header of the CSV should not be hard coded in the tool but it should be extracted from the PDF file.

### Test Code 3

You will need to compare both the `Investments-2.csv` as well as Investments-2-PnL.csv to ensure that the output is correct.

On Linux and macOS:

```bash
diff output/Investments-2.csv reference/Investments-2.csv
```

or for Windows:

```bash
FC output/Investments-2.csv reference/Investments-2.csv
```

The output of the above command should be empty for your solution to pass.

## Step 4: Read and Clean the Misaligned Data PDF

You need to write a tool that reads `input/Investments-3.pdf` and writes an XLSX conversion of the PDF to `output/Investments-3.xlsx`.

This PDF file will have some of the stock names in a different vertical alignment. The header is also a multi-level header, i.e., the header will have a cell that spans multiple columns.

You need to ensure in the final XLSX file that the `Purchase` header is grouped above the `Date Purchased`, `Shares Purchased`, and `Purchase Price/Share` headers as follows:

![Purchase Header](assets/Purchase%20Header.png)

Similarly, the `Sale` header should be grouped above `Date Sold` and `Sale Price/Share` headers like follows:

![Sale Header](assets/Sale%20Header.png)

The command to run the tool should look like this:

```bash
<program> convert_misaligned_data --input input/Investments-3.pdf --output output/Investments-3.xlsx
```

Please calculate the profit or loss of the stocks that were sold as instructed in [Step 2](#step-2-calculate-profit-and-loss-pnl).

Please ensure that the output Excel file matches the above header setup and that the number of rows in the final Excel file is 40.
