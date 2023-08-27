
 # Time :  4 h

 class Size_string
    attr_accessor   :in, :out, :test, :size, :index, :string

    def size_string

        @string = ARGV[0].start_with? ("")
        puts "string : #{@string}"

        @in       = ARGV.count
        puts "in     : #{ARGV.class}"

        @index    
        puts "index  : #{@index}"

            if !(@in == 1) 
                puts "if out : erreur."
            else 
                @out  = ARGV[0].length     
            puts "if in  : #{@in}"
            puts "if out : #{@out}"
            end                

    end
end

if __FILE__ == $0 
    ss = Size_string.new

    ss.size_string
end

