import argparse

welcome = "Practicing creating interactive command-line interfaces"

parser = argparse.ArgumentParser(description=welcome)
parser.add_argument(
    "--domain",
    "-d",
    required=True,
    help='domain name of the website you want to scrape. i.e. “https://ahadsheriff.com"',
)


args = parser.parse_args()


print("##########################")
print(args.domain)
