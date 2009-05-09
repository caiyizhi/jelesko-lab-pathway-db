class BlastForm(forms.Form):

    seq = forms.CharField(widget=forms.Textarea)
    evalue = forms.FloatField(initial=1)
    wordsize = forms.IntegerField(
            label='Word Size',
            initial=3
    )
    database_option = forms.ChoiceField(
            label='Database',
            choices=BLAST_DBS,
            initial=INITIAL_DB_CHOICE
    )
