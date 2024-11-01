namespace التحويل_بين_انظمة_العد
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.guna2DragControl1 = new Guna.UI2.WinForms.Guna2DragControl(this.components);
            this.guna2PictureBox1 = new Guna.UI2.WinForms.Guna2PictureBox();
            this.GunatxtInput = new Guna.UI2.WinForms.Guna2TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.btnBin = new Guna.UI2.WinForms.Guna2GradientButton();
            this.btnHex = new Guna.UI2.WinForms.Guna2GradientButton();
            this.lable2 = new System.Windows.Forms.Label();
            this.btnDec = new Guna.UI2.WinForms.Guna2GradientButton();
            this.label3 = new System.Windows.Forms.Label();
            this.btnOct = new Guna.UI2.WinForms.Guna2GradientButton();
            this.label4 = new System.Windows.Forms.Label();
            this.guna2ControlBox1 = new Guna.UI2.WinForms.Guna2ControlBox();
            this.guna2ControlBox2 = new Guna.UI2.WinForms.Guna2ControlBox();
            this.lblTypeInput = new System.Windows.Forms.Label();
            this.guna2ComboBox1 = new Guna.UI2.WinForms.Guna2ComboBox();
            this.guna2GradientCircleButton1 = new Guna.UI2.WinForms.Guna2GradientCircleButton();
            ((System.ComponentModel.ISupportInitialize)(this.guna2PictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // guna2DragControl1
            // 
            this.guna2DragControl1.DockIndicatorTransparencyValue = 0.6D;
            this.guna2DragControl1.TargetControl = this;
            this.guna2DragControl1.UseTransparentDrag = true;
            // 
            // guna2PictureBox1
            // 
            this.guna2PictureBox1.Image = global::التحويل_بين_انظمة_العد.Properties.Resources.images__2_;
            this.guna2PictureBox1.ImageRotate = 0F;
            this.guna2PictureBox1.Location = new System.Drawing.Point(-1, -4);
            this.guna2PictureBox1.Name = "guna2PictureBox1";
            this.guna2PictureBox1.Size = new System.Drawing.Size(97, 537);
            this.guna2PictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.guna2PictureBox1.TabIndex = 1;
            this.guna2PictureBox1.TabStop = false;
            // 
            // GunatxtInput
            // 
            this.GunatxtInput.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.GunatxtInput.BorderRadius = 12;
            this.GunatxtInput.BorderThickness = 3;
            this.GunatxtInput.Cursor = System.Windows.Forms.Cursors.IBeam;
            this.GunatxtInput.DefaultText = "";
            this.GunatxtInput.DisabledState.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(208)))), ((int)(((byte)(208)))), ((int)(((byte)(208)))));
            this.GunatxtInput.DisabledState.FillColor = System.Drawing.Color.FromArgb(((int)(((byte)(226)))), ((int)(((byte)(226)))), ((int)(((byte)(226)))));
            this.GunatxtInput.DisabledState.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(138)))), ((int)(((byte)(138)))), ((int)(((byte)(138)))));
            this.GunatxtInput.DisabledState.PlaceholderForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(138)))), ((int)(((byte)(138)))), ((int)(((byte)(138)))));
            this.GunatxtInput.FocusedState.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(94)))), ((int)(((byte)(148)))), ((int)(((byte)(255)))));
            this.GunatxtInput.Font = new System.Drawing.Font("Segoe UI", 13.8F);
            this.GunatxtInput.ForeColor = System.Drawing.Color.Purple;
            this.GunatxtInput.HoverState.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(94)))), ((int)(((byte)(148)))), ((int)(((byte)(255)))));
            this.GunatxtInput.Location = new System.Drawing.Point(350, 107);
            this.GunatxtInput.Margin = new System.Windows.Forms.Padding(5, 6, 5, 6);
            this.GunatxtInput.Name = "GunatxtInput";
            this.GunatxtInput.PasswordChar = '\0';
            this.GunatxtInput.PlaceholderText = "";
            this.GunatxtInput.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
            this.GunatxtInput.SelectedText = "";
            this.GunatxtInput.Size = new System.Drawing.Size(352, 51);
            this.GunatxtInput.TabIndex = 2;
            this.GunatxtInput.TextChanged += new System.EventHandler(this.GunatxtInput_TextChanged);
            // 
            // label1
            // 
            this.label1.Font = new System.Drawing.Font("Tahoma", 13F, System.Drawing.FontStyle.Bold);
            this.label1.Location = new System.Drawing.Point(111, 392);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 41);
            this.label1.TabIndex = 3;
            this.label1.Text = "Bin";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // btnBin
            // 
            this.btnBin.BackColor = System.Drawing.Color.Transparent;
            this.btnBin.BorderRadius = 12;
            this.btnBin.BorderThickness = 2;
            this.btnBin.DisabledState.BorderColor = System.Drawing.Color.DarkGray;
            this.btnBin.DisabledState.CustomBorderColor = System.Drawing.Color.DarkGray;
            this.btnBin.DisabledState.FillColor = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnBin.DisabledState.FillColor2 = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnBin.DisabledState.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(141)))), ((int)(((byte)(141)))), ((int)(((byte)(141)))));
            this.btnBin.FillColor = System.Drawing.Color.RoyalBlue;
            this.btnBin.Font = new System.Drawing.Font("Segoe UI", 13F, System.Drawing.FontStyle.Bold);
            this.btnBin.ForeColor = System.Drawing.Color.White;
            this.btnBin.Location = new System.Drawing.Point(178, 392);
            this.btnBin.Name = "btnBin";
            this.btnBin.Size = new System.Drawing.Size(307, 41);
            this.btnBin.TabIndex = 4;
            this.btnBin.Text = "0";
            this.btnBin.Click += new System.EventHandler(this.guna2GradientButton1_Click);
            // 
            // btnHex
            // 
            this.btnHex.BackColor = System.Drawing.Color.Transparent;
            this.btnHex.BorderRadius = 12;
            this.btnHex.BorderThickness = 2;
            this.btnHex.DisabledState.BorderColor = System.Drawing.Color.DarkGray;
            this.btnHex.DisabledState.CustomBorderColor = System.Drawing.Color.DarkGray;
            this.btnHex.DisabledState.FillColor = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnHex.DisabledState.FillColor2 = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnHex.DisabledState.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(141)))), ((int)(((byte)(141)))), ((int)(((byte)(141)))));
            this.btnHex.FillColor = System.Drawing.Color.RoyalBlue;
            this.btnHex.Font = new System.Drawing.Font("Segoe UI", 13F, System.Drawing.FontStyle.Bold);
            this.btnHex.ForeColor = System.Drawing.Color.White;
            this.btnHex.Location = new System.Drawing.Point(178, 257);
            this.btnHex.Name = "btnHex";
            this.btnHex.Size = new System.Drawing.Size(307, 41);
            this.btnHex.TabIndex = 6;
            this.btnHex.Text = "0";
            // 
            // lable2
            // 
            this.lable2.Font = new System.Drawing.Font("Tahoma", 13F, System.Drawing.FontStyle.Bold);
            this.lable2.Location = new System.Drawing.Point(111, 257);
            this.lable2.Name = "lable2";
            this.lable2.Size = new System.Drawing.Size(61, 41);
            this.lable2.TabIndex = 5;
            this.lable2.Text = "Hex";
            // 
            // btnDec
            // 
            this.btnDec.BackColor = System.Drawing.Color.Transparent;
            this.btnDec.BorderRadius = 12;
            this.btnDec.BorderThickness = 2;
            this.btnDec.DisabledState.BorderColor = System.Drawing.Color.DarkGray;
            this.btnDec.DisabledState.CustomBorderColor = System.Drawing.Color.DarkGray;
            this.btnDec.DisabledState.FillColor = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnDec.DisabledState.FillColor2 = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnDec.DisabledState.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(141)))), ((int)(((byte)(141)))), ((int)(((byte)(141)))));
            this.btnDec.FillColor = System.Drawing.Color.RoyalBlue;
            this.btnDec.Font = new System.Drawing.Font("Segoe UI", 13F, System.Drawing.FontStyle.Bold);
            this.btnDec.ForeColor = System.Drawing.Color.White;
            this.btnDec.Location = new System.Drawing.Point(178, 182);
            this.btnDec.Name = "btnDec";
            this.btnDec.Size = new System.Drawing.Size(307, 41);
            this.btnDec.TabIndex = 10;
            this.btnDec.Text = "0";
            // 
            // label3
            // 
            this.label3.Font = new System.Drawing.Font("Tahoma", 13F, System.Drawing.FontStyle.Bold);
            this.label3.Location = new System.Drawing.Point(111, 182);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(61, 41);
            this.label3.TabIndex = 9;
            this.label3.Text = "DEC";
            // 
            // btnOct
            // 
            this.btnOct.BackColor = System.Drawing.Color.Transparent;
            this.btnOct.BorderRadius = 12;
            this.btnOct.BorderThickness = 2;
            this.btnOct.DisabledState.BorderColor = System.Drawing.Color.DarkGray;
            this.btnOct.DisabledState.CustomBorderColor = System.Drawing.Color.DarkGray;
            this.btnOct.DisabledState.FillColor = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnOct.DisabledState.FillColor2 = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.btnOct.DisabledState.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(141)))), ((int)(((byte)(141)))), ((int)(((byte)(141)))));
            this.btnOct.FillColor = System.Drawing.Color.RoyalBlue;
            this.btnOct.Font = new System.Drawing.Font("Segoe UI", 13F, System.Drawing.FontStyle.Bold);
            this.btnOct.ForeColor = System.Drawing.Color.White;
            this.btnOct.Location = new System.Drawing.Point(178, 324);
            this.btnOct.Name = "btnOct";
            this.btnOct.Size = new System.Drawing.Size(307, 41);
            this.btnOct.TabIndex = 8;
            this.btnOct.Text = "0";
            // 
            // label4
            // 
            this.label4.Font = new System.Drawing.Font("Tahoma", 13F, System.Drawing.FontStyle.Bold);
            this.label4.Location = new System.Drawing.Point(111, 324);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(61, 41);
            this.label4.TabIndex = 7;
            this.label4.Text = "OCT";
            // 
            // guna2ControlBox1
            // 
            this.guna2ControlBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.guna2ControlBox1.Animated = true;
            this.guna2ControlBox1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.guna2ControlBox1.BorderColor = System.Drawing.Color.Magenta;
            this.guna2ControlBox1.BorderThickness = 2;
            this.guna2ControlBox1.Cursor = System.Windows.Forms.Cursors.Hand;
            this.guna2ControlBox1.FillColor = System.Drawing.Color.White;
            this.guna2ControlBox1.Font = new System.Drawing.Font("Tahoma", 10F);
            this.guna2ControlBox1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.guna2ControlBox1.IconColor = System.Drawing.Color.Black;
            this.guna2ControlBox1.Location = new System.Drawing.Point(826, 12);
            this.guna2ControlBox1.Name = "guna2ControlBox1";
            this.guna2ControlBox1.PressedColor = System.Drawing.Color.White;
            this.guna2ControlBox1.Size = new System.Drawing.Size(45, 29);
            this.guna2ControlBox1.TabIndex = 11;
            // 
            // guna2ControlBox2
            // 
            this.guna2ControlBox2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.guna2ControlBox2.Animated = true;
            this.guna2ControlBox2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.guna2ControlBox2.BorderColor = System.Drawing.Color.Magenta;
            this.guna2ControlBox2.BorderThickness = 2;
            this.guna2ControlBox2.ControlBoxType = Guna.UI2.WinForms.Enums.ControlBoxType.MinimizeBox;
            this.guna2ControlBox2.Cursor = System.Windows.Forms.Cursors.Hand;
            this.guna2ControlBox2.FillColor = System.Drawing.Color.White;
            this.guna2ControlBox2.Font = new System.Drawing.Font("Tahoma", 10F);
            this.guna2ControlBox2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.guna2ControlBox2.IconColor = System.Drawing.Color.Black;
            this.guna2ControlBox2.Location = new System.Drawing.Point(766, 12);
            this.guna2ControlBox2.Name = "guna2ControlBox2";
            this.guna2ControlBox2.PressedColor = System.Drawing.Color.White;
            this.guna2ControlBox2.Size = new System.Drawing.Size(45, 29);
            this.guna2ControlBox2.TabIndex = 12;
            // 
            // lblTypeInput
            // 
            this.lblTypeInput.Font = new System.Drawing.Font("Tahoma", 13F, System.Drawing.FontStyle.Bold);
            this.lblTypeInput.Location = new System.Drawing.Point(248, 27);
            this.lblTypeInput.Name = "lblTypeInput";
            this.lblTypeInput.Size = new System.Drawing.Size(134, 30);
            this.lblTypeInput.TabIndex = 13;
            this.lblTypeInput.Text = "Type input";
            // 
            // guna2ComboBox1
            // 
            this.guna2ComboBox1.BackColor = System.Drawing.Color.Transparent;
            this.guna2ComboBox1.BorderColor = System.Drawing.Color.BlueViolet;
            this.guna2ComboBox1.BorderRadius = 10;
            this.guna2ComboBox1.BorderThickness = 3;
            this.guna2ComboBox1.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.guna2ComboBox1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.guna2ComboBox1.FocusedColor = System.Drawing.Color.FromArgb(((int)(((byte)(94)))), ((int)(((byte)(148)))), ((int)(((byte)(255)))));
            this.guna2ComboBox1.FocusedState.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(94)))), ((int)(((byte)(148)))), ((int)(((byte)(255)))));
            this.guna2ComboBox1.Font = new System.Drawing.Font("Segoe UI", 13F);
            this.guna2ComboBox1.ForeColor = System.Drawing.Color.Black;
            this.guna2ComboBox1.ItemHeight = 30;
            this.guna2ComboBox1.Items.AddRange(new object[] {
            "Decimal",
            "Binary",
            "Octal",
            "Hexadecimal"});
            this.guna2ComboBox1.Location = new System.Drawing.Point(178, 71);
            this.guna2ComboBox1.Name = "guna2ComboBox1";
            this.guna2ComboBox1.Size = new System.Drawing.Size(176, 36);
            this.guna2ComboBox1.StartIndex = 0;
            this.guna2ComboBox1.TabIndex = 14;
            this.guna2ComboBox1.SelectedIndexChanged += new System.EventHandler(this.GunatxtInput_TextChanged);
            // 
            // guna2GradientCircleButton1
            // 
            this.guna2GradientCircleButton1.Animated = true;
            this.guna2GradientCircleButton1.DisabledState.BorderColor = System.Drawing.Color.DarkGray;
            this.guna2GradientCircleButton1.DisabledState.CustomBorderColor = System.Drawing.Color.DarkGray;
            this.guna2GradientCircleButton1.DisabledState.FillColor = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.guna2GradientCircleButton1.DisabledState.FillColor2 = System.Drawing.Color.FromArgb(((int)(((byte)(169)))), ((int)(((byte)(169)))), ((int)(((byte)(169)))));
            this.guna2GradientCircleButton1.DisabledState.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(141)))), ((int)(((byte)(141)))), ((int)(((byte)(141)))));
            this.guna2GradientCircleButton1.FillColor2 = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.guna2GradientCircleButton1.Font = new System.Drawing.Font("Segoe UI", 14F, System.Drawing.FontStyle.Bold);
            this.guna2GradientCircleButton1.ForeColor = System.Drawing.Color.White;
            this.guna2GradientCircleButton1.Location = new System.Drawing.Point(587, 384);
            this.guna2GradientCircleButton1.Name = "guna2GradientCircleButton1";
            this.guna2GradientCircleButton1.ShadowDecoration.Mode = Guna.UI2.WinForms.Enums.ShadowMode.Circle;
            this.guna2GradientCircleButton1.Size = new System.Drawing.Size(69, 49);
            this.guna2GradientCircleButton1.TabIndex = 16;
            this.guna2GradientCircleButton1.Text = "1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(883, 529);
            this.Controls.Add(this.guna2GradientCircleButton1);
            this.Controls.Add(this.guna2ComboBox1);
            this.Controls.Add(this.lblTypeInput);
            this.Controls.Add(this.guna2ControlBox2);
            this.Controls.Add(this.guna2ControlBox1);
            this.Controls.Add(this.btnDec);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.btnOct);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.btnHex);
            this.Controls.Add(this.lable2);
            this.Controls.Add(this.btnBin);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.GunatxtInput);
            this.Controls.Add(this.guna2PictureBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.guna2PictureBox1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private Guna.UI2.WinForms.Guna2DragControl guna2DragControl1;
        private Guna.UI2.WinForms.Guna2PictureBox guna2PictureBox1;
        private Guna.UI2.WinForms.Guna2GradientButton btnBin;
        private System.Windows.Forms.Label label1;
        private Guna.UI2.WinForms.Guna2TextBox GunatxtInput;
        private Guna.UI2.WinForms.Guna2GradientButton btnDec;
        private System.Windows.Forms.Label label3;
        private Guna.UI2.WinForms.Guna2GradientButton btnOct;
        private System.Windows.Forms.Label label4;
        private Guna.UI2.WinForms.Guna2GradientButton btnHex;
        private System.Windows.Forms.Label lable2;
        private Guna.UI2.WinForms.Guna2ControlBox guna2ControlBox1;
        private Guna.UI2.WinForms.Guna2ComboBox guna2ComboBox1;
        private System.Windows.Forms.Label lblTypeInput;
        private Guna.UI2.WinForms.Guna2ControlBox guna2ControlBox2;
        private Guna.UI2.WinForms.Guna2GradientCircleButton guna2GradientCircleButton1;
    }
}

