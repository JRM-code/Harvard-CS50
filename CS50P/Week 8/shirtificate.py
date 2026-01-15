from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", "C", 75, 190)
        self.set_font("helvetica", "", 40)
        self.cell(190, 60, "CS50 Shirtificate", border=0, align="C")
     

def main():
    name = input("Enter your name: ")
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=30)
    pdf.set_text_color(255)
    pdf.cell(-190, 250, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()
