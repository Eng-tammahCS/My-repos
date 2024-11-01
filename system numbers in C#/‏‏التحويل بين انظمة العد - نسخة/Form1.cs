using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace التحويل_بين_انظمة_العد
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void guna2GradientButton1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void GunatxtInput_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(GunatxtInput.Text))
            {
                return;
            }
            int[] types ={ 10, 2, 8, 16 };
            int num = ConvertToDecimal(GunatxtInput.Text,
                types[guna2ComboBox1.SelectedIndex]);

            btnBin.Text = Convert.ToString(num, 2);
            btnHex.Text = Convert.ToString(num, 16);
            btnOct.Text = Convert.ToString(num, 8);
            btnDec.Text = Convert.ToString(num, 10);


        }
        private int ConvertToDecimal(string Input,int Basesystem)
        {
            int Resault = 0;
            int power = 1;

            for (int i = Input.Length-1; i >=0; i--)
            {
            int A ;

                if (char.IsDigit(Input[i]))
                {
                    A = Input[i] - '0';
                }
                else
                {
                    A = 10 + (Input[i] - 'A');
                }
                    Resault+=A*power;
                    power*=Basesystem;



            }
            return Resault;
        }

        private void guna2CircleButton1_Click(object sender, EventArgs e)
        {

        }
    }
}
