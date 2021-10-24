from django.db import models


# Create your models here.

class UserWallet(models.Model):
  img = models.ImageField(db_column='IMG', upload_to='users/%Y-%m-%d', max_length=500, default=None, null=True,
                          verbose_name="Imagen"),
  name = models.CharField(db_column='NickName', max_length=5000, default=None, null=True)
  wallet_address = models.CharField(db_column='Wallet', max_length=5000)
  firma = models.CharField(db_column='Firma', max_length=5000)
  start_date = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'UserWallet'

  def __str__(self):
    return 'Firma: {} \n StartDate: {} \n Wallet: {}'.format(self.firma, self.start_date, self.wallet_address)


class PoapLink(models.Model):
  linkpoap = models.FileField(db_column='linkpoaps',
                              upload_to='poap/%Y/%m/%d',
                              null=True,
                              blank=True,
                              verbose_name='Links POAPS', )

  class Meta:
    db_table = 'PoapLink'

  def __str__(self):
    return '{}'.format(self.linkpoap)


class Link(models.Model):
  link = models.CharField(db_column='Link', max_length=5000, default=None, null=True)

  class Meta:
    db_table = 'Link'

  def save(self, *args, **kwargs):
    print('save() is called.')
    super(Link, self).save(*args, **kwargs)

  def __str__(self):
    return '{}'.format(self.link)
