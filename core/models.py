from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import slugify

from user.models import User




class Company(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(_("Legal name"), max_length=250)
    address = models.TextField(_("Address"))
    city = models.CharField(_("City"), max_length=200)
    state = models.CharField(_("State"), max_length=200)
    country = models.CharField(_("Country"), max_length=200)
    pincode = models.CharField(_("Pincode"), max_length=50)
    phone = models.CharField(_("Phone no."), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    website = models.CharField(_("Website"), max_length=250)

    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companys")

    def __str__(self):
        return str(f"{self.name} - {self.city}, {self.state}, {self.country} {self.pincode}")

    def get_absolute_url(self):
        return reverse("company_detail", kwargs={"pk": self.pk})




class PrimaryGroup(models.Model):

    name = models.CharField(_("Name of group"), max_length=250)


    class Meta:
        verbose_name = _("Primary Group")
        verbose_name_plural = _("Primary Groups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("primarygroup_detail", kwargs={"pk": self.pk})




class Group(models.Model):

    name = models.CharField(_("Name of group"), max_length=250)
    under = models.ForeignKey(PrimaryGroup, verbose_name=_("Under"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return str(f"{self.name} - {self.under}")

    def get_absolute_url(self):
        return reverse("group_detail", kwargs={"pk": self.pk})




class Ledger(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(_("Name of Ledger"), max_length=250)
    under = models.ForeignKey(Group, verbose_name=_("Under"), on_delete=models.CASCADE)
    address = models.TextField(_("Address"), blank=True, null=True)
    opening = models.IntegerField(_("Opening Balance"), blank=True, null=True)




    class Meta:
        verbose_name = _("ledger")
        verbose_name_plural = _("ledgers")

    def __str__(self):
        return str(f"{self.name}")

    def get_absolute_url(self):
        return reverse("ledger_detail", kwargs={"pk": self.pk})




class Voucher(models.Model):

    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("voucher")
        verbose_name_plural = _("vouchers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("voucher_detail", kwargs={"pk": self.pk})





class Journal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, verbose_name=_("Voucher Type"), on_delete=models.CASCADE)


    date = models.DateField(_("Date"))
    sn = models.CharField(_("Voucher No."), max_length=50, blank=True, null=True)
    rn = models.CharField(_("Reference No."), max_length=50, blank=True, null=True)
    by = models.ForeignKey(Ledger, verbose_name=_("By"), on_delete=models.CASCADE, related_name="by", blank=True, null=True)
    to = models.ForeignKey(Ledger, verbose_name=_("To"), on_delete=models.CASCADE, related_name="+", blank=True, null=True) 
    nar = models.TextField(_("Narration"), blank=True, null=True)
    total = models.IntegerField(_("Amount"), blank=True, null=True)
    

    class Meta:
        verbose_name = _("journal")
        verbose_name_plural = _("journal")

    def __str__(self):
        return str(f"{self.by.name} A/c Dr, To {self.to.name} A/c - {self.voucher} Voucher")

    def get_absolute_url(self):
        return reverse("journal_detail", kwargs={"pk": self.pk})
