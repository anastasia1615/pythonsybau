from app.io.input import read_con, read_file, read_pandas
from app.io.output import print_c, write_f
def main():
    con_text = read_con()
    file_text = read_file("data/pinkmaggit.txt")
    df = read_pandas("data/thisplaceisdeath.csv")
    print_c("input from console")
    print_c(con_text)
    print_c("input from file")
    print_c(file_text)
    print_c("input with pandas")
    print_c(df.to_string(index=False))
    result_text = ("input from console:\n" + con_text+ "\n\ninput from file:\n" + file_text + "\n\ninput with pandas:\n" + df.to_string(index=False))
    write_f("data/result.txt", result_text)
if __name__ == "__main__":
    main()