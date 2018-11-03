
class Splitter(object):

    def split(self, string):

        array = []
        start = 0
        while(len(string)):

            nextDelimiter = string.find(',', start)
            openSingleQuote = string.find("'", start)
            openDoubleQuote = string.find('"', start)

            if openSingleQuote or openDoubleQuote is -1:
                nextQuote = max(openSingleQuote, openDoubleQuote)
            else:
                nextQuote = min(i for i in [openSingleQuote, openDoubleQuote] if i > 0)

            # no more delimiters, finish
            if nextDelimiter is -1:
                array.append(string)
                break

            if nextDelimiter < nextQuote or nextQuote is -1:
                # chomp segment for array
                array.append(string[:nextDelimiter])

                # remove delimiter
                string = string[nextDelimiter + 1:]

            else:
                start = string.find(string[nextQuote], nextQuote + 1) + 1

        return array
        