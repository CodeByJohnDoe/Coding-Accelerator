
 # Time :  4 h

 class Size_string
    attr_accessor   :in, :out

    def size_string

    @in     = ARGV
    puts "#{ARGV.class}"

        if !(/\A\"+\z\"/.match(ARGV[0])) 
            
            @out =  "erreur."
        else

        @out  = @in.length     

        end
        
    puts "#{@in}"
    puts "#{@out}"
    end
end

if __FILE__ == $0 
    ss = Size_string.new

    ss.size_string
end
