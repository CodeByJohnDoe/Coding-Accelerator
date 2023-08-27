
 # Time :  15 min

 class Reverse
    attr_accessor   :in, :out, :size, :index

    def reverse

    @in     = ARGV.first.split(//)
    @size   = @in.length
    @index  = 1
    @out    = []

        until  @index > @size
            out.push(@in[@size - @index])
            @index += 1
        end
        
    puts "#{@out.join}"
    end
end

if __FILE__ == $0 
    rv = Reverse.new

    rv.reverse 

end
