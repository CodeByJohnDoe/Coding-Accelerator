
# Time : 5hs

class Alphabet
    attr_accessor :letter

    # Send letter
    def send_letter
        puts "#{@letter.join}"
    end
end

if __FILE__ == $0 
    az = Alphabet.new
    
    # Listing of letter
    az.letter =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    az.send_letter
    az.letter = nil

end