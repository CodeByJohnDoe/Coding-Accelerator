
 # Time :  2 h 

 class Peer
    attr_accessor   :argument, :numbers, :type, :num_check


    def compare
    
    @argument   = ARGV[0].to_i
    @type       = ARGV[0] !~ num_check


        if (ARGV[0] =~ @numbers ) == nil || (@type == false)
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

    pe.numbers   = /[0-9]/
    pe.num_check = /\D/
    pe.compare  
end