def generateTable(num):
    htmlTable = ""

    htmlTable += "<table border=\"1\">\n"
    htmlTable += "<tr>\n"
    htmlTable += "<th>Number</th>\n"
    htmlTable += "<th>Multiple</th>\n"
    htmlTable += "</tr>\n"

    for i in range(1, 11):
        htmlTable += "<tr>\n"
        htmlTable += "<td>" + str(num) + "</td>\n"
        htmlTable += "<td>" + str(num * i) + "</td>\n"
        htmlTable += "</tr>\n"

    htmlTable += "</table>"

    return htmlTable