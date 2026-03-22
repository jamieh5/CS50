from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    
    pdf.set_font("Helvetica", style="B", size=50)

    # Placing the header text
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")

    # Putting the image into the pdf
    pdf.image("shirtificate.png", x="C", y=80, w=200, h=200)

    # Putting the name var into the middle of the shirt and changing the look
    pdf.set_font("Helvetica", size=35)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 180)
    pdf.cell(210, 10, f"{name} took CS50!", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()