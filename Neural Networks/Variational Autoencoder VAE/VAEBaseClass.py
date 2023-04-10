import tensorflow as tf
from tensorflow import keras
from keras import layers, models
from AutotuningToolkit import AutotuningToolkit
# Import the neurotransmitter classes
from SerotoninVAE import SerotoninVAE
from NorepinephrineVAE import NorepinephrineVAE
from GABAVAE import GABAVAE
from DopamineVAE import DopamineVAE

class VAE(tf.keras.Model):
    def __init__(self, input_dim, latent_dim, encoder_layers, decoder_layers, learning_rate=0.001):
        super(VAE, self).__init__()

        # Initialize neurotransmitter instances
        self.serotonin = SerotoninVAE(alpha=0.1)
        self.norepinephrine = NorepinephrineVAE(learning_rate=learning_rate)
        self.gaba = GABAVAE(threshold=0.5)
        self.dopamine = DopamineVAE(beta=0.001)

        self.latent_dim = latent_dim
        self.encoder = self.build_encoder(input_dim, encoder_layers, latent_dim)
        self.decoder = self.build_decoder(input_dim, decoder_layers, latent_dim)

    def build_encoder(self, input_dim, encoder_layers, latent_dim):
        inputs = layers.Input(shape=input_dim)
        x = inputs
        for layer_size in encoder_layers:
            x = layers.Dense(layer_size, activation='relu')(x)
        z_mean = layers.Dense(latent_dim)(x)
        z_log_var = layers.Dense(latent_dim)(x)
        return models.Model(inputs, (z_mean, z_log_var), name='encoder')

    def build_decoder(self, input_dim, decoder_layers, latent_dim):
        inputs = layers.Input(shape=(latent_dim,))
        x = inputs
        for layer_size in decoder_layers:
            x = layers.Dense(layer_size, activation='relu')(x)
        outputs = layers.Dense(input_dim, activation='sigmoid')(x)
        return models.Model(inputs, outputs, name='decoder')

    def reparameterize(self, z_mean, z_log_var):
        eps = tf.random.normal(shape=z_mean.shape)
        return z_mean + tf.exp(0.5 * z_log_var) * eps

    def call(self, inputs, training=None, mask=None):
        z_mean, z_log_var = self.encoder(inputs)
        z = self.reparameterize(z_mean, z_log_var)
        return self.decoder(z)

    def train_step(self, data, toolkit_report):
        # Update neurotransmitter levels based on the toolkit report
        self.serotonin.update_alpha(toolkit_report["epoch"])
        self.norepinephrine.adjust_learning_rate(toolkit_report["epoch"])
        self.gaba.threshold = toolkit_report["gaba_threshold"]
        self.dopamine.update_beta(toolkit_report["epoch"])

        with tf.GradientTape() as tape:
            z_mean, z_log_var = self.encoder(data)
            z = self.reparameterize(z_mean, z_log_var)
            x_recon = self.decoder(z)
            recon_loss = tf.reduce_mean(tf.keras.losses.binary_crossentropy(data, x_recon))
            kl_loss = -0.5 * tf.reduce_mean(1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
            total_loss = recon_loss + kl_loss
        grads = tape.gradient(total_loss, self.trainable_variables)
        optimizer = tf.keras.optimizers.Adam(lr=self.norepinephrine.learning_rate)
        optimizer.apply_gradients(zip(grads, self.trainable_variables))
        return {'loss': total_loss, 'recon_loss': recon_loss, 'kl_loss': kl_loss}

    def update_neurotransmitter_levels(self, toolkit_report):
        self.serotonin.update_alpha(toolkit_report["epoch"])
        self.norepinephrine.adjust_learning_rate(toolkit_report["epoch"])
        self.gaba.threshold = toolkit_report["gaba_threshold"]
        self.dopamine.update_beta(toolkit_report["epoch"])

    def main_adaptive_nn(self, data, toolkit_report, training_epochs):
        for epoch in range(training_epochs):
            # Update neurotransmitter levels based on the toolkit report
            self.update_neurotransmitter_levels(toolkit_report)

            # Train the neural network
            result = self.train_step(data, toolkit_report)

            # Update the toolkit report based on the training result
            toolkit_report = AutotuningToolkit.evaluate(result)

        return result

