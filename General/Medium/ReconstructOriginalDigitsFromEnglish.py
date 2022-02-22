class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        output = []
        
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] =1
            else:
                freq[s[i]] +=1 
        
        if 'z' in freq and freq['z']>0:
            for i in range(freq['z']):
                output.append(0)
            freq['e'] -= freq['z']
            freq['r'] -= freq['z']
            freq['o'] -= freq['z']
            freq['z'] = 0
            
        if 'w' in freq and freq['w']>0:
            for i in range(freq['w']):
                output.append(2)
            freq['t'] -= freq['w']
            freq['o'] -= freq['w']
            freq['w'] = 0
            
        if 'u' in freq and freq['u']>0:
            for i in range(freq['u']):
                output.append(4)
            freq['f'] -= freq['u']
            freq['o'] -= freq['u']
            freq['r'] -= freq['u']
            freq['u'] = 0
            
        if 'x' in freq and freq['x']>0:
            for i in range(freq['x']):
                output.append(6)
            freq['s'] -= freq['x']
            freq['i'] -= freq['x']
            freq['x'] = 0
            
        if 'g' in freq and freq['g']>0:
            for i in range(freq['g']):
                output.append(8)
            freq['e'] -= freq['g']
            freq['i'] -= freq['g']
            freq['h'] -= freq['g']
            freq['t'] -= freq['g']
            freq['g'] = 0
            
        if 'o' in freq and freq['o']>0:
            for i in range(freq['o']):
                output.append(1)
            freq['n'] -= freq['o']
            freq['e'] -= freq['o']           
            freq['o'] = 0
            
        if 'f' in freq and freq['f']>0:
            for i in range(freq['f']):
                output.append(5)
            freq['i'] -= freq['f']
            freq['v'] -= freq['f']     
            freq['e'] -= freq['f']  
            freq['f'] = 0
            
        if 's' in freq and freq['s']>0:
            for i in range(freq['s']):
                output.append(7)
            freq['e'] -= freq['s'] * 2
            freq['v'] -= freq['s']     
            freq['n'] -= freq['s']  
            freq['s'] = 0
            
        if 't' in freq and freq['t']>0:
            for i in range(freq['t']):
                output.append(3)
            freq['e'] -= freq['t'] * 2
            freq['h'] -= freq['t']     
            freq['r'] -= freq['t']  
            freq['t'] = 0
            
        if 'i' in freq and freq['i']>0:
            for i in range(freq['i']):
                output.append(9)
            freq['n'] -= freq['i'] * 2
            freq['e'] -= freq['i']   
            freq['i'] = 0
            
        newStr = ""
        for i in sorted(output):
            newStr = newStr + str(i)
        return newStr