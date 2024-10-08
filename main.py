
def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        rows=['']*numRows
        cur_row=0
        step=-1

        for i in s:
            rows[cur_row]+=i
            if cur_row==0 or cur_row==numRows-1:
                step= -step
            cur_row+=step

        return ''.join(rows)

string="PAYPALISHIRING"
rows=3
word=convert(string,rows)
print(word)