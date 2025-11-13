from pyscript import display, HTML

socsci_club = {"John", "Darren", "Agnes", "Emily"}
art_club = {"Gerald", "Sophia", "Robert", "Vincent"}

# 1. Students in at least one club
at_least_one = socsci_club | art_club

# 2. Students in both clubs
both_clubs = socsci_club & art_club

# 3. Students only in the first club
only_socsci = socsci_club - art_club

# 4. Students only in the second club
only_art = art_club - socsci_club

# 5. Students in exactly one club
exactly_one = socsci_club ^ art_club

output = f"""
<h5>SocSci Club:</h5> {', '.join(socsci_club)}<br>
<h5>Art Club:</h5> {', '.join(art_club)}<br><hr>

<p><strong>Students in at least one club:</strong> {', '.join(at_least_one)}</p>
<p><strong>Students in both clubs:</strong> {', '.join(both_clubs)}</p>
<p><strong>Students only in SocSci Club:</strong> {', '.join(only_socsci)}</p>
<p><strong>Students only in Art Club:</strong> {', '.join(only_art)}</p>
<p><strong>Students in exactly one club:</strong> {', '.join(exactly_one)}</p>
"""

display(HTML(output))
