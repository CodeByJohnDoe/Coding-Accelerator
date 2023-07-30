
 # Time :  15 min

 class Reverse
    attr_accessor   :in, :out, :size, :index

    def reverse

    @in     = ARGV.first.split(//)
    @size   = @in.length
    @index  = 1

    until  @index > @size

        @out  = @out.add(@in[(@size - @index)])
        @index += 1
        puts "eees"
    end
        
    puts "#{ARGV}"
    puts "#{@in}"
    puts "#{@size}"
    puts "#{@out}"
    end
end

if __FILE__ == $0 
    rv = Reverse.new

    rv.reverse 

end
