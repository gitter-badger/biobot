from willie import module

from Bio.Seq import Seq
from Bio.Alphabet import generic_nucleotide

from Bio.SeqUtils import MeltingTemp


@module.commands('melting')
def melting(bot, trigger):
  sequence = trigger.group(2)
  if sequence == "" or sequence is None:
    bot.say("Why you asking for the melting temp of nuffin? you some sort of idiot")
  else:
    s = Seq(sequence.strip(), generic_nucleotide)
    bot.say("melting temp of "+sequence+" is "+str(MeltingTemp.Tm_staluc(s)))

#def

#print("%0.2f" % MeltingTemp.Tm_staluc(s))

#print("%0.2f" % MeltingTemp.Tm_staluc(s, rna=True))


