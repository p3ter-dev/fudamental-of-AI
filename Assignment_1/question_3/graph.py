graph = {
    'Addis Ababa': [('Adama', 3), ('Ambo', 5), ('Debre Birhan', 5)],
    'Ambo': [('Addis Ababa', 5), ('Wolkite', 6), ('Nekemte', 9)],
    'Nekemte': [('Ambo', 9), ('Bedele', 0), ('Gimbi', 4)],
    'Gimbi': [('Nekemte', 4), ('Dembi Dollo', 6)],
    'Dembi Dollo': [('Gambela', 4), ('Assosa', 12), ('Gimbi', 6)],
    'Gambela': [('Dembi Dollo', 4), ('Gore', 5)],
    'Gore': [('Gambela', 5), ('Tepi', 9), ('Bedele', 6)],
    'Tepi': [('Gore', 9), ('Bonga', 8), ('Mizan Teferi', 4)],
    'Mizan Teferi': [('Tepi', 4), ('Bonga', 4)],
    'Bonga': [('Mizan Teferi', 4), ('Tepi', 8), ('Dawro', 10), ('Jimma', 4)],
    'Dawro': [('Bonga', 10), ('Wolaita sodo', 6)],
    'Wolaita sodo': [('Dawro', 6), ('Arba Minch', 0), ('Hossana', 4)],
    'Arba Minch': [('Wolaita sodo', 7), ('Basketo', 10), ('Konso', 4)],
    'Basketo': [('Arba Minch', 10), ('Bench Maji', 5)],
    'Hossana': [('Wolaita sodo', 4), ('Shashemene', 7), ('Worabe', 2)],
    'Worabe': [('Hossana', 2), ('Wolkite', 5), ('Butta Jira', 2)],
    'Wolkite': [('Worabe', 5), ('Ambo', 6), ('Jimma', 8)],
    'Butta Jira': [('Worabe', 2), ('Batu', 2)],
    'Batu': [('Butta Jira', 2), ('Shashemene', 3), ('Adama', 4)],
    'Adama': [('Batu', 4), ('Addis Ababa', 3), ('Matahara', 3), ('Assela', 4)],
    'Assela': [('Adama', 4), ('Assasa', 4)],
    'Assasa': [('Assela', 4), ('Dodolla', 1)],
    'Dodolla': [('Shashemene', 3), ('Bale', 3)],
    'Shashemene': [('Dodolla', 3), ('Hawassa', 1), ('Batu', 3), ('Hossana', 7)],
    'Hawassa': [('Shashemene', 1), ('Dilla', 3)],
    'Matahara': [('Adama', 3), ('Awash', 1)],
    'Awash': [('Matahara', 1), ('Chiro', 4), ('Gambi Rasu', 5)],
    'Chiro': [('Awash', 4), ('Dire Dawa', 8)],
    'Dire Dawa': [('Chiro', 8), ('Harar', 4)],
    'Gambi Rasu': [('Awash', 5), ('Samara', 9)],
    'Samara': [('Gambi Rasu', 9), ('Woldia', 8), ('Alamata', 11), ('Fanti Rasu', 7)],
    'Fanti Rasu': [('Samara', 7), ('Kilbet Rasu', 6)],
    'Woldia': [('Samara', 8), ('Lalibela', 7), ('Alamata', 3), ('Dessie', 6)],
    'Dessie': [('Woldia', 6), ('Kemise', 4)],
    'Kemise': [('Dessie', 4), ('Debre Sina', 6)],
    'Debre Sina': [('Kemise', 6), ('Debre Birhan', 2), ('Debre Markos', 17)],
    'Debre Birhan': [('Addis Ababa', 5), ('Debre Sina', 2)],
    'Debre Markos': [('Debre Sina', 17), ('Finote Selam', 3)],
    'Finote Selam': [('Debre Markos', 3), ('Bahir Dar', 6), ('Injibara', 2)],
    'Injibara': [('Finote Selam', 2), ('Bahir Dar', 4)],
    'Bahir Dar': [('Injibara', 4), ('Finote Selam', 6), ('Metekel', 11), ('Azezo', 7), ('Debre Tabor', 4)],
    'Azezo': [('Bahir Dar', 7), ('Gondar', 1), ('Metema', 7)],
    'Metema': [('Azezo', 7), ('Gondar', 7), ('Kartum', 19)],
    'Gondar': [('Azezo', 1), ('Metema', 7), ('Debark', 4), ('Humera', 9)],
    'Debark': [('Gondar', 4), ('Shire', 7)],
    'Shire': [('Debark', 7), ('Humera', 8), ('Axum', 2)],
    'Axum': [('Shire', 2), ('Adwa', 1), ('Asmara', 5)],
    'Debre Tabor': [('Bahir Dar', 4), ('Lalibela', 8)],
    'Lalibela': [('Debre Tabor', 8), ('Woldia', 7), ('Sekota', 6)],
    'Sekota': [('Lalibela', 6), ('Alamata', 6), ('Mekele', 9)],
    'Alamata': [('Sekota', 6), ('Woldia', 3), ('Samara', 11), ('Mekele', 5)],
    'Mekele': [('Alamata', 5), ('Sekota', 9), ('Adwa', 7), ('Adigrat', 4)],
    'Adwa': [('Mekele', 7), ('Axum', 1), ('Adigrat', 4)],
    'Adigrat': [('Mekele', 4), ('Asmera', 6), ('Adwa', 4)],
    'Metekel': [('Bahir Dar', 11)],
    'Dilla': [('Hawassa', 3), ('Bule Hora', 4)],
    'Bule Hora': [('Dilla', 4), ('Yabello', 3)],
    'Yabello': [('Bule Hora', 3), ('Konso', 3), ('Moyale', 6)],
    'Konso': [('Yabello', 3), ('Arba Minch', 4)],
    'Dodolla': [('Shashemene', 3), ('Bale', 13), ('Assasa', 1)],
    'Bale': [('Dodolla', 13), ('Goba', 18), ('Liben', 11), ('Sof Oumer', 23)],
    'Sof Oumer': [('Bale', 23), ('Goba', 6), ('Gode', 23)],
    'Gode': [('Sof Oumer', 23), ('Kebri Dehar', 5), ('Dollo', 17), ('Mokadisho', 22)],
    'Kebri Dehar': [('Gode', 5), ('Werder', 6), ('Dega Habur', 6)],
    'Dega Habur': [('Kebri Dehar', 6), ('Jijiga', 5)],
    'Jijiga': [('Dega Habur', 5), ('Babile', 3)],
    'Babile': [('Jijiga', 3), ('Harar', 2), ('Goba', 28)],
    'Harar': [('Dire Dawa', 4), ('Babile', 2)],
    'Goba': [('Bale', 18), ('Babile', 28), ('Sof Oumer', 6)],
    'Jimma': [('Bonga', 4), ('Wolkite', 8), ('Bedele', 7)],
    'Bench Maji': [('Basketo', 5), ('Juba', 22)],
    'Dollo': [('Gode', 17)],
    'Liben': [('Bale', 11)],
    'Moyale': [('Yabello', 6), ('Nairobi', 22)],
    'Bedele': [('Nekemte', 0), ('Jimma', 7), ('Gore', 6)],
    'Humera': [('Gondar', 9), ('Shire', 8), ('Kartum', 21)],
    'Kilbet Rasu': [('Fanti Rasu', 6)],
    'Werder': [('Kebri Dehar', 6)],
    'Juba': [('Bench Maji', 22)],
}
