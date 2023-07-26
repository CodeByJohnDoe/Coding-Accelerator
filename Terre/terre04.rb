
 # Time :  2 h 

 class Peer
    attr_accessor   :argument, :numbers
        
    @argument = ARGV[0].to_i


    def is_number (num_given)
        !!Integer {num_given} rescue false 
    end


    def compare

        if (ARGV[0] =~ @numbers ) == nil
            puts "Tu ne me la mettra pas à l'envers."          

        else    
            if (@argument % 2 == 0)
                puts "pair"     
                
            else (@argument % 2 == 1)
                puts "impair"     

            end
        end
    end
end

if __FILE__ == $0 
    pe = Peer.new

    pe.numbers = /[0-9]/
    
    pe.is_number (@argument)
    pe.compare  
end