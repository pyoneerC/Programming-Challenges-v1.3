<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <!-- define the output format -->
  <xsl:output method="pdf" media-type="application/pdf" />
  
  <!-- define the page dimensions -->
  <xsl:template match="/">
    <fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
      <fo:layout-master-set>
        <fo:simple-page-master master-name="a4" page-height="29.7cm" page-width="21cm" margin-top="1cm" margin-bottom="1cm" margin-left="2cm" margin-right="2cm">
          <fo:region-body />
        </fo:simple-page-master>
      </fo:layout-master-set>
      <fo:page-sequence master-reference="a4">
        <fo:flow flow-name="xsl-region-body">
          <!-- add the customer data to the document -->
          <xsl:apply-templates select="customers/customer" />
        </fo:flow>
      </fo:page-sequence>
    </fo:root>
  </xsl:template>
  
  <!-- define the customer data format -->
  <xsl:template match="customer">
    <fo:block font-size="12pt" margin-bottom="10pt">
      <fo:inline font-weight="bold">Name:</fo:inline> <xsl:value-of select="name" /><fo:block />
      <fo:inline font-weight="bold">Email:</fo:inline> <xsl:value-of select="email" /><fo:block />
      <fo:inline font-weight="bold">Phone:</fo:inline> <xsl:value-of select="phone" /><fo:block />
    </fo:block>
  </xsl:template>

</xsl:stylesheet>