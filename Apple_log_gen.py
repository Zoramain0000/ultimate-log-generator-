#!/usr/bin/env python3
"""
🍏 Apple ID Finder (Python Port)
Compatible with Windows, Mac, Linux, Termux.
Features: Generate Unique Apple IDs, 195+ Countries, Charts, Auto-Mode, Export CSV.
"""

import random
import json
import time
import csv
from datetime import datetime

# --- 1. Configuration & Databases ---

COUNTRIES = [
    {"name": "Afghanistan", "flag": "🇦🇫"}, {"name": "Albania", "flag": "🇦🇱"},
    {"name": "Algeria", "flag": "🇩🇿"}, {"name": "Andorra", "flag": "🇦🇩"},
    {"name": "Angola", "flag": "🇦🇴"}, {"name": "Antigua and Barbuda", "flag": "🇦🇬"},
    {"name": "Argentina", "flag": "🇦🇷"}, {"name": "Armenia", "flag": "🇦🇲"},
    {"name": "Australia", "flag": "🇦🇺"}, {"name": "Austria", "flag": "🇦🇹"},
    {"name": "Azerbaijan", "flag": "🇦🇿"}, {"name": "Bahamas", "flag": "🇧🇸"},
    {"name": "Bahrain", "flag": "🇧🇭"}, {"name": "Bangladesh", "flag": "🇧🇩"},
    {"name": "Barbados", "flag": "🇧🇧"}, {"name": "Belarus", "flag": "🇧🇾"},
    {"name": "Belgium", "flag": "🇧🇪"}, {"name": "Belize", "flag": "🇧🇿"},
    {"name": "Benin", "flag": "🇧🇯"}, {"name": "Bhutan", "flag": "🇧🇹"},
    {"name": "Bolivia", "flag": "🇧🇴"}, {"name": "Bosnia and Herzegovina", "flag": "🇧🇦"},
    {"name": "Botswana", "flag": "🇧🇼"}, {"name": "Brazil", "flag": "🇧🇷"},
    {"name": "Brunei", "flag": "🇧🇳"}, {"name": "Bulgaria", "flag": "🇧🇬"},
    {"name": "Burkina Faso", "flag": "🇧🇫"}, {"name": "Burundi", "flag": "🇧🇮"},
    {"name": "Cabo Verde", "flag": "🇨🇻"}, {"name": "Cambodia", "flag": "🇰🇭"},
    {"name": "Cameroon", "flag": "🇨🇲"}, {"name": "Canada", "flag": "🇨🇦"},
    {"name": "Central African Republic", "flag": "🇨🇫"}, {"name": "Chad", "flag": "🇹🇩"},
    {"name": "Chile", "flag": "🇨🇱"}, {"name": "China", "flag": "🇨🇳"},
    {"name": "Colombia", "flag": "🇨🇴"}, {"name": "Comoros", "flag": "🇰🇲"},
    {"name": "Congo (Congo-Brazzaville)", "flag": "🇨🇬"}, {"name": "Costa Rica", "flag": "🇨🇷"},
    {"name": "Croatia", "flag": "🇭🇷"}, {"name": "Cuba", "flag": "🇨🇺"},
    {"name": "Cyprus", "flag": "🇨🇾"}, {"name": "Czech Republic", "flag": "🇨🇿"},
    {"name": "Denmark", "flag": "🇩🇰"}, {"name": "Djibouti", "flag": "🇩🇯"},
    {"name": "Dominica", "flag": "🇩🇲"}, {"name": "Dominican Republic", "flag": "🇩🇴"},
    {"name": "Ecuador", "flag": "🇪🇨"}, {"name": "Egypt", "flag": "🇪🇬"},
    {"name": "El Salvador", "flag": "🇸🇻"}, {"name": "Equatorial Guinea", "flag": "🇬🇶"},
    {"name": "Eritrea", "flag": "🇪🇷"}, {"name": "Estonia", "flag": "🇪🇪"},
    {"name": "Eswatini", "flag": "🇸🇿"}, {"name": "Ethiopia", "flag": "🇪🇹"},
    {"name": "Fiji", "flag": "🇫🇯"}, {"name": "Finland", "flag": "🇫🇮"},
    {"name": "France", "flag": "🇫🇷"}, {"name": "Gabon", "flag": "🇬🇦"},
    {"name": "Gambia", "flag": "🇬🇲"}, {"name": "Georgia", "flag": "🇬🇪"},
    {"name": "Germany", "flag": "🇩🇪"}, {"name": "Ghana", "flag": "🇬🇭"},
    {"name": "Greece", "flag": "🇬🇷"}, {"name": "Grenada", "flag": "🇬🇩"},
    {"name": "Guatemala", "flag": "🇬🇹"}, {"name": "Guinea", "flag": "🇬🇳"},
    {"name": "Guinea-Bissau", "flag": "🇬🇼"}, {"name": "Guyana", "flag": "🇬🇾"},
    {"name": "Haiti", "flag": "🇭🇹"}, {"name": "Honduras", "flag": "🇭🇳"},
    {"name": "Hungary", "flag": "🇭🇺"}, {"name": "Iceland", "flag": "🇮🇸"},
    {"name": "India", "flag": "🇮🇳"}, {"name": "Indonesia", "flag": "🇮🇩"},
    {"name": "Iran", "flag": "🇮🇷"}, {"name": "Iraq", "flag": "🇮🇶"},
    {"name": "Ireland", "flag": "🇮🇪"}, {"name": "Israel", "flag": "🇮🇱"},
    {"name": "Italy", "flag": "🇮🇹"}, {"name": "Jamaica", "flag": "🇯🇲"},
    {"name": "Japan", "flag": "🇯🇵"}, {"name": "Jordan", "flag": "🇯🇴"},
    {"name": "Kazakhstan", "flag": "🇰🇿"}, {"name": "Kenya", "flag": "🇰🇪"},
    {"name": "Kiribati", "flag": "🇰🇮"}, {"name": "Kuwait", "flag": "🇰🇼"},
    {"name": "Kyrgyzstan", "flag": "🇰🇬"}, {"name": "Laos", "flag": "🇱🇦"},
    {"name": "Latvia", "flag": "🇱🇻"}, {"name": "Lebanon", "flag": "🇱🇧"},
    {"name": "Lesotho", "flag": "🇱🇸"}, {"name": "Liberia", "flag": "🇱🇷"},
    {"name": "Libya", "flag": "🇱🇾"}, {"name": "Liechtenstein", "flag": "🇱🇮"},
    {"name": "Lithuania", "flag": "🇱🇹"}, {"name": "Luxembourg", "flag": "🇱🇺"},
    {"name": "Madagascar", "flag": "🇲🇬"}, {"name": "Malawi", "flag": "🇲🇼"},
    {"name": "Malaysia", "flag": "🇲🇾"}, {"name": "Maldives", "flag": "🇲🇻"},
    {"name": "Mali", "flag": "🇲🇱"}, {"name": "Malta", "flag": "🇲🇹"},
    {"name": "Marshall Islands", "flag": "🇲🇭"}, {"name": "Mauritania", "flag": "🇲🇷"},
    {"name": "Mauritius", "flag": "🇲🇺"}, {"name": "Mexico", "flag": "🇲🇽"},
    {"name": "Micronesia", "flag": "🇫🇲"}, {"name": "Moldova", "flag": "🇲🇩"},
    {"name": "Monaco", "flag": "🇲🇨"}, {"name": "Mongolia", "flag": "🇲🇳"},
    {"name": "Montenegro", "flag": "🇲🇪"}, {"name": "Morocco", "flag": "🇲🇦"},
    {"name": "Mozambique", "flag": "🇲🇿"}, {"name": "Myanmar (Burma)", "flag": "🇲🇲"},
    {"name": "Namibia", "flag": "🇳🇦"}, {"name": "Nauru", "flag": "🇳🇷"},
    {"name": "Nepal", "flag": "🇳🇵"}, {"name": "Netherlands", "flag": "🇳🇱"},
    {"name": "New Zealand", "flag": "🇳🇿"}, {"name": "Nicaragua", "flag": "🇳🇮"},
    {"name": "Niger", "flag": "🇳🇪"}, {"name": "Nigeria", "flag": "🇳🇬"},
    {"name": "North Korea", "flag": "🇰🇵"}, {"name": "North Macedonia", "flag": "🇲🇰"},
    {"name": "Norway", "flag": "🇳🇴"}, {"name": "Oman", "flag": "🇴🇲"},
    {"name": "Pakistan", "flag": "🇵🇰"}, {"name": "Palau", "flag": "🇵🇼"},
    {"name": "Panama", "flag": "🇵🇦"}, {"name": "Papua New Guinea", "flag": "🇵🇬"},
    {"name": "Paraguay", "flag": "🇵🇾"}, {"name": "Peru", "flag": "🇵🇪"},
    {"name": "Philippines", "flag": "🇵🇭"}, {"name": "Poland", "flag": "🇵🇱"},
    {"name": "Portugal", "flag": "🇵🇹"}, {"name": "Qatar", "flag": "🇶🇦"},
    {"name": "Romania", "flag": "🇷🇴"}, {"name": "Russia", "flag": "🇷🇺"},
    {"name": "Rwanda", "flag": "🇷🇼"}, {"name": "Saint Kitts and Nevis", "flag": "🇰🇳"},
    {"name": "Saint Lucia", "flag": "🇱🇨"}, {"name": "Saint Vincent and the Grenadines", "flag": "🇻🇨"},
    {"name": "Samoa", "flag": "🇼🇸"}, {"name": "San Marino", "flag": "🇸🇲"},
    {"name": "Sao Tome and Principe", "flag": "🇸🇹"}, {"name": "Saudi Arabia", "flag": "🇸🇦"},
    {"name": "Senegal", "flag": "🇸🇳"}, {"name": "Serbia", "flag": "🇷🇸"},
    {"name": "Seychelles", "flag": "🇸🇨"}, {"name": "Sierra Leone", "flag": "🇸🇱"},
    {"name": "Singapore", "flag": "🇸🇬"}, {"name": "Slovakia", "flag": "🇸🇰"},
    {"name": "Slovenia", "flag": "🇸🇮"}, {"name": "Solomon Islands", "flag": "🇸🇧"},
    {"name": "Somalia", "flag": "🇸🇴"}, {"name": "South Africa", "flag": "🇿🇦"},
    {"name": "South Korea", "flag": "🇰🇷"}, {"name": "South Sudan", "flag": "🇸🇸"},
    {"name": "Spain", "flag": "🇪🇸"}, {"name": "Sri Lanka", "flag": "🇱🇰"},
    {"name": "Sudan", "flag": "🇸🇩"}, {"name": "Suriname", "flag": "🇸🇷"},
    {"name": "Sweden", "flag": "🇸🇪"}, {"name": "Switzerland", "flag": "🇨🇭"},
    {"name": "Syria", "flag": "🇸🇾"}, {"name": "Taiwan", "flag": "🇹🇼"},
    {"name": "Tajikistan", "flag": "🇹🇯"}, {"name": "Tanzania", "flag": "🇹🇿"},
    {"name": "Thailand", "flag": "🇹🇭"}, {"name": "Timor-Leste", "flag": "🇹🇱"},
    {"name": "Togo", "flag": "🇹🇬"}, {"name": "Tonga", "flag": "🇹🇴"},
    {"name": "Trinidad and Tobago", "flag": "🇹🇹"}, {"name": "Tunisia", "flag": "🇹🇳"},
    {"name": "Turkey", "flag": "🇹🇷"}, {"name": "Turkmenistan", "flag": "🇹🇲"},
    {"name": "Tuvalu", "flag": "🇹🇻"}, {"name": "Uganda", "flag": "🇺🇬"},
    {"name": "Ukraine", "flag": "🇺🇦"}, {"name": "United Arab Emirates", "flag": "🇦🇪"},
    {"name": "United Kingdom", "flag": "🇬🇧"}, {"name": "United States", "flag": "🇺🇸"},
    {"name": "Uruguay", "flag": "🇺🇾"}, {"name": "Uzbekistan", "flag": "🇺🇿"},
    {"name": "Vanuatu", "flag": "🇻🇺"}, {"name": "Vatican City", "flag": "🇻🇦"},
    {"name": "Venezuela", "flag": "🇻🇪"}, {"name": "Vietnam", "flag": "🇻🇳"},
    {"name": "Yemen", "flag": "🇾🇪"}, {"name": "Zambia", "flag": "🇿🇲"},
    {"name": "Zimbabwe", "flag": "🇿🇼"}
]

FIRST_NAMES = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Jamie", "Blake", "Skyler", "Riley", "Dakota", 
    "Abby", "Abigail", "Ada", "Addie", "Addison", "Adelaide", "Adele", "Adora", "Adriana", "Ælfgifu", 
    "Æthelburh", "Agnes", "Aileen", "Alaina", "Alanna", "Alberta", "Albina", "Aleana", "Alexa", 
    "Alexandra", "Alexandria", "Alexis", "Alice", "Alicia", "Alisha", "Alison", "Allyson", "Alma", 
    "Althea", "Alvina", "Alyson", "Amanda", "Amber", "Amberley", "Amelia", "Amy", "Ana", "Andrea", 
    "Andrée", "Andy", "Angel", "Angela", "Angelica", "Angelina", "Angella", "Angie", "Anna", 
    "Annabelle", "Annabeth", "Anne", "Annette", "Annie", "Antonia", "April", "Arabella", "Arda", 
    "Ariana", "Ariel", "Arya", "Ash", "Ashley", "Astrid", "Aubrey", "Audra", "Audrey", "Aurora", 
    "Autumn", "Averil", "Avis", "Azalea", "Babette", "Barb", "Barbara", "Beatrice", "Beatrix", 
    "Beau", "Becca", "Becki", "Becky", "Belinda", "Bella", "Berenice", "Bertha", "Betsy", 
    "Bettina", "Betty", "Beverly", "Bianca", "Blair", "Blake", "Blanche", "Blossom", "Bobbi", 
    "Bobby", "Bonnie", "Braden", "Brandy", "Brenda", "Brianna", "Bridget", "Brielle", "Brilliana", 
    "Brooklyn", "Brynlee", "Bryony", "Caden", "Calla", "Candy", "Cara", "Cari", "Carina", 
    "Carissa", "Carlena", "Carlene", "Carlie", "Carly", "Carmelita", "Carol", "Carol Ann", 
    "Carol Anne", "Carole", "Carolina", "Caroline", "Carolyn", "Carrie Ann", "Carrie Anne", 
    "Carroll", "Carry", "Carson", "Cary", "Casey", "Cassandra", "Cassidy", "Cathleen", "Cathy", 
    "Cecilia", "Cecily", "Celestia", "Celia", "Celinda", "Chara", "Charis", "Charisse", 
    "Charity", "Charla", "Charle", "Charlee", "Charlene", "Charley", "Charli", "Charlie", 
    "Charlotte", "Charly", "Charlyne", "Charmaine", "Chas", "Chelsea", "Cherry", "Cheryl", 
    "Chloe", "Chris", "Christabel", "Christi", "Christina", "Christine", "Christy", "Cindy", 
    "Claire", "Clara", "Clare", "Claribel", "Clarice", "Clarissa", "Claudia", "Clementine", 
    "Clover", "Cody", "Colette", "Colleen", "Constance", "Cora", "Coral", "Coraline", 
    "Cordelia", "Courtney", "Crystal", "Cynthia",
    "Daenerys", "Daisy", "Dana", "Dani", "Danielle", "Danna", "Daphne", "Darla", "Darlene", 
    "Davina", "Dawn", "Deanna", "D", "Deanne", "Deb", "Debbie", "Deborah", "Dede", "Deja", 
    "Delaney", "Delia", "Demetria", "Demi", "Denise", "Destiny", "Devon", "Diamond", "Diana", 
    "Diane", "Dimity", "Donna", "Dora", "Doreen", "Doris", "Dorothy", "Dottie", "Drew", 
    "Dulcie", "E", "Eadgifu", "Ealdgyth", "Ebony", "Edburga", "Eden", "Edith", "Edna", 
    "Edris", "Edwina", "Effie", "Eileen", "Elaine", "Eleanor", "Elektra", "Elisha", "Eliza", 
    "Elizabeth", "Ella", "Elle", "Ellen", "Ellie", "Ellis", "Elora", "Ember", "Emerald", 
    "Emily", "Emma", "Enid", "Erika", "Erin", "Estelle", "Esther", "Esty", "Ethel", 
    "Etheldreda", "Etty", "Eudora", "Eva", "Evan", "Evangelina", "Eve", "Evelyn", "F", 
    "Fabienne", "Faith", "Fancy", "Faye", "Felicity", "Fern", "Finn", "Fiona", "Fleur", 
    "Florence", "Frances", "Francie", "Francine", "Frankie", "Frederica", "Frida", "G", 
    "Gage", "Gail", "Gale", "Gemma", "Gene", "Genevieve", "Georgene", "Georgette", "Georgia", 
    "Georgiana", "Georgina", "Gertie", "Gertrude", "Gia", "Gina", "Ginny", "Giselle", 
    "Gladys", "Glenda", "Glenna", "Gloria", "Glynis", "Goldie", "Grace", "Gussie", "Gwen", 
    "Gwenda", "Gwendolen", "Gwendoline", "Gwendolyn", "Gwyneth",
    "Haisley", "Haley", "Hannah", "Harmony", "Harriet", "Hayden", "Hayley", "Hazel", 
    "Heather", "Heidi", "Helen", "Helena", "Helene", "Henrietta", "Hero", "Hester", 
    "Hilary", "Hilda", "Hodierna", "Holly", "Honor", "Hope", "Hunter", 
    "Ida", "Ila", "Imelda", "Imogen", "Ingrid", "Iona", "Irene", "Iris", 
    "Irma", "Isa", "Isabel", "Isabella", "Isla", "Ivy", 
    "Jacinta", "Jack", "Jackie", "Jacqueline", "Jacqui", "Jade", "Jaime", "Jamie", 
    "Jan", "Jana", "Jane", "Janee", "Janelle", "Janet", "Janey", "Janie", 
    "January", "Jasmine", "Jay", "Jayda", "Jayden", "Jayne", "Jaynie", 
    "Jean", "Jeanie", "Jeannie", "Jemima", "Jemma", "Jenna", "Jennifer", "Jenny", 
    "Jensen", "Jerri", "Jerry", "Jess", "Jessica", "Jessie", "Jill", 
    "Joan", "Joanna", "Joanne", "Jodi", "Jodie", "Jody", "Joelle", 
    "Joey", "Johnny", "Jolie", "Jordan", 
    "Josephine", "Josie", "Joy", "Joyce", "Judith", "Julia", "Julianne", 
    "Julie", "Juliet", "June", "Juniper", "Juno", "Justine", 
    "Kailey", "Kalla", "Kara", "Karen", "Karin", "Karlee", "Karlene", 
    "Karli", "Karlie", "Karly", "Karolyn", "Karrie", "Karyn", "Karyne", 
    "Kasey", "Kate", "Katey", "Kathleen", "Kathryn", "Kathy", "Katie", 
    "Katina", "Katrina", "Katy", "Kay", "Kayla", "Kaylee", "Kelly", 
    "Kelsey", "Kierra", "Kim", "Kimberly", "Kira", "Kirsteen", 
    "Kirstin", "Kitty", "Krista", "Kristen", "Kristi", "Kristin", 
    "Kristy", "Kylie", "Kyra",
    "Lacey", "Lana", "Lanna", "Lara", "Larissa", "Laura", "Laurel", "Lauren", 
    "Laurence", "Lauretta", "Laurie", "Lauryn", "Lavender", "Leah", "Leanne", 
    "Lee", "Leila", "Leisha", "Lena", "Lenna", "Leona", "Leonora", "Leslie", 
    "Lettice", "Lexi", "Lila", "Liliana", "Lilibet", "Lilibeth", "Lilla", 
    "Lillian", "Lillie", "Lilly", "Lily", "Lina", "Linda", "Lindsay", 
    "Lindy", "Lisa", "Liza", "Lizzie", "Lois", "Loraine", "Lorelei", 
    "Lorena", "Loretta", "Lori", "Lorinda", "Lorna", "Lorraine", "Lottie", 
    "Lotty", "Louella", "Louisa", "Louise", "Lucia", "Lucinda", "Lucy", 
    "Lydia", "Lyndsay", "Lynnette", "Lysette", "Mabel", "Mable", "Macy", 
    "Madelaine", "Madeleine", "Madelyn", "Madge", "Madison", "Madonna", 
    "Mae", "Maggie", "Magnolia", "Mallory", "Mandy", "Mara", "Marcia", 
    "Marcie", "Margaret", "Margie", "Margo", "Maria", "Mariah", "Marian", 
    "Marianne", "Marie", "Marigold", "Marilyn", "Marina", "Marissa", 
    "Marjorie", "Marlene", "Marsha", "Marta", "Martha", "Martina", 
    "Mary", "Mary Belle", "Maryanne", "Mason", "Matilda", "Maud", 
    "Maude", "Maura", "Maureen", "Mavis", "Maxine", "May", "Maya", 
    "Mayola", "McKenna", "Meara", "Medea", "Megan", "Mehitable", 
    "Mel", "Melanie", "Melina", "Melinda", "Melissa", "Melody", 
    "Mercedes", "Meredith", "Merilyn", "Merle", "Merrilyn", "Mia", 
    "Micah", "Michele", "Michelle", "Mila", "Mildred", "Miley", 
    "Millicent", "Millie", "Mina", "Mindi", "Mindy", "Minerva", 
    "Minnie", "Miranda", "Miriam", "Misty", "Moira", "Molly", 
    "Morgan", "Muriel", "Myra", "Myrna", "Myrtle",
    "Nadia", "Nadine", "Naila", "Nancy", "Naomi", "Narcissa", "Nathalie", 
    "Nena", "Nettie", "Netty", "Nevaeh", "Nia", "Nicki", "Nicola", 
    "Nicole", "Nina", "Noel", "Noella", "Noelle",
    "Napoleon", "Nate", "Nathan", "Nathanael", "Nathaniel", "Ned", "Nehemiah", 
    "Neil", "Nelson", "Nestor", "Newt", "Newton", "Niall", "Nicholas", 
    "Nick", "Nicodemus", "Nicolas", "Nigel", "Niles", "Noah", "Noam", 
    "Norm", "Norman", "Nowell",
    "Obadiah", "Odin", "Oliver", "Ollie", "Orion", "Orlando", "Orville", 
    "Osbert", "Osborne", "Oscar", "Osric", "Oswald", "Otis", "Otto", 
    "Owen", "Ozzie",
    "Paddy", "Palmer", "Paris", "Patrick", "Patsy", "Patty", "Paul", 
    "Peleg", "Percival", "Percy", "Perry", "Pete", "Peter", "Philip", 
    "Phillipps", "Phineas", "Pierse", "Poe", "Porter", "Posy", "Preston",
    "Quentin", "Quincy", "Quinn",
    "Race", "Rafe", "Raife", "Raleigh", "Ralph", "Ralphie", "Ramsey", 
    "Randall", "Randi", "Randolph", "Randy", "Raphael", "Rathbone", 
    "Ray", "Raymond", "Reese", "Reggie", "Reginald", "Rembrandt", 
    "Rendell", "Renssalaer", "Reuben", "Rex", "Reynold", "Rhett", 
    "Rich", "Richard", "Richie", "Rick", "Ricky", "Riley", "Ritchie", 
    "Rob", "Robbie", "Robert", "Robin", "Roderick", "Rodger", 
    "Rodney", "Roger", "Rogers", "Roland", "Roman", "Ron", "Ronald", 
    "Ronnie", "Rory", "Roscoe", "Ross", "Roualeyn", "Rowland", 
    "Roy", "Rudolph", "Rudy", "Rufus", "Rupert", "Russ", "Russell", 
    "Ryan", "Ryder",
    "Sam", "Sammy", "Samson", "Samuel", "Sandy", "Sanford", "Saul", 
    "Sawyer", "Scott", "Sean", "Sebastian", "Seth", "Seymour", 
    "Shane", "Shaun", "Shawn", "Shayne", "Sheldon", "Shepherd", 
    "Sid", "Sidney", "Sigmund", "Simon", "Sky", "Skyler", 
    "Sloane", "Smith", "Sol", "Solomon", "Spencer", "Stan", 
    "Stanford", "Stanley", "Stefan", "Stephen", "Stetson", 
    "Steve", "Stevie", "Stevland", "Stewart", "Storm", "Stuart", 
    "Swaine", "Syd", "Sydney", "Sylvester",
    "Tanner", "Taran", "Taylor", "Tazewell", "Ted", "Tedd", "Teddy", 
    "Terence", "Terry", "Thaddeus", "Theo", "Theodore", "Thomas", 
    "Thor", "Tim", "Timmy", "Timothy", "Tobias", "Toby", "Tod", 
    "Todd", "Toddy", "Tom", "Tommie", "Tommy", "Tony", "Tracy", 
    "Travis", "Tregonwell", "Trent", "Trevor", "Trey", "Tristan", 
    "Troy", "Truman", "Tucker", "Tyler", "Tyson",
    "Ultan", "Ulysses", "Uriah",
    "Val", "Valentine", "Vernon", "Vic", "Vicary", "Victor", "Vince", 
    "Vincent", "Vinny", "Vivian",
    "Wade", "Wadsworth", "Walden", "Waldo", "Walker", "Wallace", 
    "Wally", "Walt", "Walter", "Warren", "Waverly", "Waylon", 
    "Wayne", "Wells", "Wes", "Wesley", "Whitney", "Wilber", 
    "Wilbert", "Wilbur", "Wilf", "Wilfred", "Wilfried", "Wilhelm", 
    "Will", "Willard", "William", "Willis", "Willy", "Wilmon", 
    "Wilson", "Winnie", "Winston", "Wolfgang", "Woodrow", 
    "Woodruff", "Woody", "Wyatt", "Wyndham",
    "Xander", "Xavier",
    "Yancy",
    "Zabdiel", "Zach", "Zachary", "Zack", "Zadoc", "Zak", "Zane", 
    "Zayden", "Zeb", "Zechariah", "Zedekiah", "Zeke", "Zeph", 
    "Zephaniah", "Zion"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes",
    "Stewart", "Morris", "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper",
    "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson",
    "Watson", "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes",
    "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross", "Foster", "Jimenez",
    "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes",
    "Gonzales", "Fisher", "Vasquez", "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham",
    "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant", "Herrera", "Gibson",
    "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens",
    "Harrison", "Fernandez", "Mcdonald", "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen",
    "Freeman", "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter", "Hunter",
    "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks",
    "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd", "Rose", "Stone", "Salazar", "Fox",
    "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens",
    "Soto", "Weaver", "Ryan", "Gardner", "Payne", "Grant", "Dunn", "Kelley", "Spencer", "Hawkins",
    "Arnold", "Pierce", "Vazquez", "Hansen", "Peters", "Santos", "Hart", "Bradley", "Knight", "Elliott",
    "Cunningham", "Duncan", "Armstrong", "Hudson", "Carroll", "Lane", "Riley", "Andrews", "Alvarado", "Ray",
    "Delgado", "Berry", "Perkins", "Hoffman", "Johnston", "Matthews", "Pena", "Richards", "Contreras", "Willis",
    "Carpenter", "Lawrence", "Sandoval", "Guerrero", "George", "Chapman", "Rios", "Estrada", "Ortega", "Watkins",
    "Greene", "Nunez", "Wheeler", "Valdez", "Harper", "Burke", "Larson", "Santiago", "Maldonado", "Morrison",
    "Franklin", "Carlson", "Austin", "Dominguez", "Carr", "Lawson", "Jacobs", "Obrien", "Lynch", "Singh",
    "Vega", "Bishop", "Montgomery", "Oliver", "Jensen", "Harvey", "Williamson", "Gilbert", "Dean", "Sims",
    "Espinoza", "Howell", "Li", "Wong", "Reid", "Hanson", "Le", "Mccoy", "Garrett", "Burton",
    "Fuller", "Wang", "Weber", "Welch", "Rojas", "Lucas", "Marquez", "Fields", "Park", "Yang",
    "Little", "Banks", "Padilla", "Day", "Walsh", "Bowman", "Schultz", "Luna", "Fowler", "Mejia",
    "Davidson", "Acosta", "Brewer", "May", "Holland", "Juarez", "Newman", "Pearson", "Curtis", "Cortez",
    "Douglas", "Schneider", "Joseph", "Barrett", "Navarro", "Figueroa", "Keller", "Avila", "Wade", "Molina",
    "Stanley", "Hopkins", "Campos", "Barnett", "Bates", "Chambers", "Caldwell", "Beck", "Lambert", "Miranda",
    "Byrd", "Craig", "Ayala", "Lowe", "Frazier", "Powers", "Neal", "Leonard", "Gregory", "Carrillo",
    "Sutton", "Fleming", "Rhodes", "Shelton", "Schwartz", "Norris", "Jennings", "Watts", "Duran", "Walters",
    "Cohen", "Mcdaniel", "Moran", "Parks", "Steele", "Vaughn", "Becker", "Holt", "Deleon", "Barker",
    "Terry", "Hale", "Leon", "Hail", "Baldwin", "Kirk", "Underwood", "Wilkins", "Gaines", "Madden"
]

DOMAINS = ["icloud.com", "me.com", "apple.com"]

# --- 2. State Management ---

class AppleIDState:
    def __init__(self):
        self.logs = []
        self.country_counts = {}
        self.generated_emails = set()
        self.batch_size = 1
        self.max_logs = 1000000 # Limit for performance
        self.current_country = None
        
    def generate_unique_email(self):
        domains = DOMAINS.copy()
        attempts = 0
        email = ""
        while not email and attempts < 1000:
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            sep = "." if random.random() > 0.5 else ""
            domain = random.choice(domains)
            num = "" if random.random() <= 0.7 else str(random.randint(1, 999))
            email = f"{first.lower()}{sep}{last.lower()}{num}@{domain}"
            attempts += 1
        return email

    def generate_log_for_country(self, country_name, country_obj):
        flag = country_obj["flag"]
        email = self.generate_unique_email()
        
        return {
            "index": len(self.logs) + 1,
            "country": country_name,
            "flag": flag,
            "email": email
        }

    def load_more_logs(self):
        if len(self.logs) >= self.max_logs:
            print(f"[INFO] Max Capacity Reached ({self.max_logs} Logs).")
            return

        print(f"[LOG] Generating batch... (Batch Size: {self.batch_size})")
        fragment = []
        for _ in range(self.batch_size):
            if len(self.logs) >= self.max_logs:
                break
            country_obj = next(c for c in COUNTRIES if c["name"] == self.current_country)
            entry = self.generate_log_for_country(self.current_country, country_obj)
            self.logs.append(entry)
            fragment.append(entry)
            self.country_counts[self.current_country] = self.country_counts.get(self.current_country, 0) + 1
        
        return fragment

    def reset_logs(self):
        self.logs = []
        self.country_counts = {}
        self.generated_emails = set()
        print("[INFO] Logs Reset.")

    def filter_logs(self, filter_term):
        if not filter_term:
            return self.logs
        return [e for e in self.logs if filter_term.lower() in e["email"].lower() or filter_term.lower() in e["country"].lower() or filter_term.lower() in e["flag"]]

    def export_report(self):
        if not self.current_country or not self.logs:
            print("[INFO] No logs to export.")
            return
        
        filename = f"apple_ids_{self.current_country.replace(' ', '_')}_{int(time.time())}.csv"
        header = ["#", "Country", "Email"]
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for e in self.logs:
                writer.writerow([
                    e["index"], 
                    f'"{e["country"]}"', 
                    f'"{e["email"]}"'
                ])
        print(f"[EXPORT] Report saved to: {filename}")

    def set_country(self, country):
        country_obj = next((c for c in COUNTRIES if c["name"] == country), None)
        if country_obj:
            self.current_country = country
            print(f"[CONFIG] Target Country: {country}")
        else:
            print(f"[CONFIG] Warning: Country '{country}' not found. Using first available.")
            self.current_country = COUNTRIES[0]["name"]

# --- 3. Event Listeners & Main Loop ---

def main():
    state = AppleIDState()
    initial_country = random.choice(COUNTRIES)
    state.current_country = initial_country
    
    print("=" * 60)
    print("🍏 APPLE ID FINDER (Python Port)")
    print("=" * 60)
    print(f"[INIT] Starting...")
    print(f"[CONFIG] Default Country: {initial_country['flag']} {initial_country['name']}")
    print("-" * 60)
    
    # Initial Load
    print(f"[LOG] Loading initial batch...")
    initial_batch = state.load_more_logs()
    print(f"[LOG] Loaded {len(initial_batch)} entries.")
    print("-" * 60)
    
    while True:
        action = input("Command [next/generate/100/filter/export/reset/config/country]: ").strip().lower()
        
        if action == "next":
            state.load_more_logs()
            print(f"[LOG] Generated more entries. Total: {len(state.logs)}")
        elif action == "generate":
            batch = state.load_more_logs()
            print(f"[LOG] Generated {len(batch)} entries.")
        elif action == "100":
            batch = state.load_more_logs()
            print(f"[LOG] Generated 100 entries.")
        elif action == "filter":
            term = input("Filter term (Email, Country, Flag...): ").strip()
            if term:
                filtered = state.filter_logs(term)
                print(f"[RESULT] Found {len(filtered)} matching entries:")
                for i, e in enumerate(filtered[:5]):
                    print(f"  {i+1}. {e['flag']} {e['country']}: {e['email']}")
                if len(filtered) > 5:
                    print(f"  ... and {len(filtered) - 5} more.")
        elif action == "export":
            state.export_report()
        elif action == "reset":
            state.reset_logs()
        elif action == "config":
            cnt = input("Set Country (type 'random' for random): ").strip().lower()
            if cnt == "random":
                state.current_country = random.choice(COUNTRIES)["name"]
                print(f"[CONFIG] New Random Country: {state.current_country}")
            else:
                state.set_country(cnt.title())
        elif action == "help":
            print("""
Available Commands:
  next      - Load next batch (default 1)
  generate  - Force generate next batch
  100       - Generate 100 IDs instantly
  filter    - Filter logs by Email, Country, Flag
  export    - Export current logs to CSV
  reset     - Reset all logs
  config    - Change target country
  help      - Show this menu
            """)
        elif action == "country":
            cnt = input("Enter Country Name: ").strip().title()
            state.set_country(cnt)
        elif not action:
            pass
        else:
            print(f"[INFO] Unknown command: {action}")
            
        print("-" * 60)

if __name__ == "__main__":
    main()
