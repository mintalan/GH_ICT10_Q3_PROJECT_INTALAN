from pyscript import display, document


def show_players(e):
    document.getElementById("output").innerHTML = ""

    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    players = [] 


    if grade == "Grade 11":

        if section == "Amorsolo":
            players = [
                "Alexander Alban", "Rocco Almeda", "Marco Ang", "Ysabel Aquino",
                "Ethan Bacolor", "Mikaela Bidayan", "Jaimee Bonoan",
                "Alyanna Cainglet", "Vivienne Canlas", "Isabella Cruz",
                "Gabrielle Dimayuga", "Danniela Farmer", "Mavic Ferreras",
                "Danielle Gonzales", "Sophia Hidalgo", "Anna Ko",
                "Kenneth Matulac", "Jiance Mercado", "Mikee Ore",
                "Alexa Salcedo", "Eun-Seong Shim", "Julia Simbul",
                "David Vergel", "Jamilla Yuson"
            ]

        elif section == "Luna":
            players = [
                "Carl Ang", "Alfredo Barretto", "Areef Batara", "Carl Bitancor",
                "Joaquin Buencamino", "Francis Cacayorin", "Sasha Campo",
                "Derrick Congmon", "Ralph Cuenca", "Irene Datugan",
                "Maxine Diestro", "Caitlin Esguerra", "Reina Fortaleza",
                "Balian Guardacasa", "Zoe Laquindanum", "Camillah Mangondato",
                "Juan Marcoleta", "Francezka Panopio", "Liesl Pascual",
                "Clara Sabanal", "Sukhjaan Singh", "Chelsea Ty",
                "Aniela Valdez"
            ]

        elif section == "Hidalgo":
            players = [
                "Raffy Bocarie", "Gian Borja", "Aiden Calo", "Abigail De Dios",
                "Elijah De Leon", "Ethan Gonzales", "Remiel Giulianna",
                "Arief Hadjisalic", "Alex Holgado", "Rory Isip",
                "Satchi Jao", "Junhee Kim", "Wisdom Rafer",
                "Zedric Ramirez", "Blaize Sanchez", "Matteo Santiago",
                "Jawad Sarip", "Pilar Sebastian", "Wencir Sumalde",
                "Victoria Turqueza"
            ]

        else:
            players = ["No list available."]


    elif grade == "Grade 10":

        if section == "Sapphire":
            players = [
                "Tessa Aseo", "Anakin Batac", "Neriza Calanglang",
                "Aaron Dee", "Vito De Guzman", "Harvey Dolor",
                "Adrianna Garces", "Selena Galvez", "Jillian Grospe",
                "Eduardo Hizon", "Margo Intalan", "Atasha Ko",
                "Alijah Lagman", "Marcus Law", "Sittie Macabago",
                "Euan Martinez", "Kelsey Medina", "Michaela Mendoza",
                "Manuel Mergal", "Seth Ngo", "Sofia Padojinog",
                "Jennifer Uy", "Ishan Shrestha", "Francesca Yao"
            ]

        elif section == "Ruby":
            players = [
                "Agena, Vada", "Ala, Zipporah Alvarado", "Baring, Jaiyanah",
                "Baylon, Koby Martin Eusebio", "Brodhagen, Alexandria Dominic",
                "Cabatingan, Jade Louisse Castro",
                "Cañete, Tarcisius John Coballes",
                "Dimaculangan, Zakari Dwayne U.",
                "Evangelista, Dwayne Kyle",
                "Galang, Charlize Liana Maceda",
                "Garabiles, Shalanie Lanette",
                "Gonzales, Amanda Mathea",
                "Jamet, Frances Hailey Almoro",
                "Ledesma, Aisha Ashley Opallia",
                "Nacino, Samantha Gabrielle",
                "Nardo, Kaitlyn Francesca",
                "Oliveros, Joaquin Rafael",
                "Olmedo, Cerinne Kimberlee",
                "Ong, Raiden Bryce Chan",
                "Rebadulla, Samantha Erin",
                "Reyes, David Miguel A.",
                "Sangreo, Vanna Marie",
                "Villafuerte, Lauren Mary",
                "Villegas, Enzo Kelsey",
                "Yao, Amanda Praise Kho"
            ]

        elif section == "Emerald":
            players = [
                "Andrian Joseph Abayon", "Erin Gayle Antes",
                "Caitlyn Apostol", "Kyla Limuelle Banaag",
                "Oscar Robert Barrientos", "Clarisse Yvonne Casal",
                "Thomas Taylor Coeli", "Ivan Kelly David",
                "Aurelia De Mata", "Franzeska Adienna Dela Cruz",
                "Jalena Rhein Dela Cruz", "Keisha May Dellejero",
                "Hikary Fukuda", "Ashley Rose Gozum",
                "Juanico Matthew Ibay", "Angela Bridget Lim",
                "Maria Julie Ann Lozano", "James Micah Mamauag",
                "Sofia Navarro", "Yciar Precones",
                "Gino Benedict Ramos", "Gurnoor Singh Sidhu",
                "Julia Ysabel Tiu", "Erich Jasmine Villamayor",
                "Annika Coleen Zaragoza"
            ]

        else:
            players = ["No list available yet."]

    for name in players:
        display(name, target="output")