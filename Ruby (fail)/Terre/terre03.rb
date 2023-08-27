
 # Time : 1 h 20

 class Alphabet_Cuter
    attr_accessor   :cursor, :end_cursor, :letters

    # Cursors
    def cursors
        @cursor         =   letters.index(ARGV[0])
        @end_cursor     =   letters.length
    end

    # Send letters
    def send_letters
        puts "#{@letters.slice(@cursor..@end_cursor).join}"
    end
end

if __FILE__ == $0 
    ac = Alphabet_Cuter.new

    ac.letters =('a'..'z').to_a.each {|letter|}
    ac.cursors
    ac.send_letters

end
