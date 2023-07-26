
 # Time :  2 h 

 class Peer
    attr_accessor   :argument, :condition
        

    puts "#{ARGV[0]}"

    @argument = ARGV[0]


    def compare

        puts "#{@argument}"
        if @argument.ascii_only?
            puts "Tu ne me la mettra pas à l'envers."    
            puts "#{2}"                      
        else
            case ARGV[0].to_i % 2

            when  0
                puts "pair"     
                puts "#{0}"  

            when 1
                puts "impair"     
                puts "#{1}"  
                    
            end
        end
    end
end


if __FILE__ == $0 
    pe = Peer.new

    pe.compare  
end